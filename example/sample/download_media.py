from twitter_openapi_python import (
    TwitterOpenapiPython,
    TimelineTimelineCursor,
    MediaExtended,
    TweetApiUtilsData,
)
from typing import Optional
import login as login
import urllib.request
import os
from pathlib import Path


cookies_dict = login.login().get_cookies().get_dict()
𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)


def media_download(tweet: TweetApiUtilsData):
    if tweet.tweet.legacy is None:
        return
    if tweet.tweet.legacy.extended_entities is None:
        return

    os.makedirs("media", exist_ok=True)
    entities = tweet.tweet.legacy.extended_entities
    media_list: list[MediaExtended] = entities.media
    for media in media_list:
        url = Path(media.media_url_https)
        data = urllib.request.urlopen(media.media_url_https).read()
        with open(Path("media", url.name), mode="wb+") as f:
            f.write(data)


user_response = 𝕏.get_user_api().get_user_by_screen_name(
    screen_name="elonmusk",
)

cursor: Optional[TimelineTimelineCursor] = None
for i in range(5):
    user_id = user_response.data.user.rest_id
    cursor_value = None if cursor is None else cursor.value
    user_media_response = 𝕏.get_tweet_api().get_user_media(
        user_id=user_id, cursor=cursor_value
    )
    if user_media_response.header.rate_limit_remaining == 0:
        print("rate_limit_remaining is 0")
        break
    cursor = user_media_response.data.cursor.bottom

    for tweet in user_media_response.data.data:
        if tweet.promoted_metadata is not None:
            continue  # skip ads
        media_download(tweet)

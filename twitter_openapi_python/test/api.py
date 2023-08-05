import json
from pathlib import Path
import twitter_openapi_python as api
import logging
from twitter_openapi_python.models import TweetApiUtilsData
from twitter_openapi_python.models.timeline import UserApiUtilsData


def get_client() -> api.TwitterOpenapiPythonClient:
    if Path("cookie.json").exists():
        with open("cookie.json", "r") as f:
            cookies_dict = json.load(f)
    else:
        raise Exception("cookie.json not found")

    client = api.TwitterOpenapiPython().get_client_from_cookies(
        ct0=cookies_dict["ct0"],
        authToken=cookies_dict["auth_token"],
    )

    return client


def print_tweet(tweet: TweetApiUtilsData) -> None:
    text = f"{tweet.user.legacy.screen_name.rjust(20)}: {tweet.tweet.legacy.full_text}"
    logging.info(text.replace("\n", " "))
    for reply in tweet.replies:
        t = f"{reply.user.legacy.screen_name.rjust(20)}: {reply.tweet.legacy.full_text}"
        logging.info(t.replace("\n", " "))


def print_user(user: UserApiUtilsData) -> None:
    legacy = user.user.legacy
    logging.info(legacy.screen_name)
    logging.info(f"listedCount: {legacy.listed_count}")
    logging.info(f"followedBy: {legacy.followed_by} following: {legacy.following}")
    text = f"friends_count: {legacy.friends_count} followers_count: {legacy.followers_count}"
    logging.info(text)
    logging.info("┄" * 50)

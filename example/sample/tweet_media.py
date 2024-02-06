import login as login
import tweepy
from twitter_openapi_python import TwitterOpenapiPython

auth_handler = login.login()
cookies_dict = auth_handler.get_cookies().get_dict()

api = tweepy.API(auth_handler)
media = api.media_upload(filename="test.png")
assert media is not None

𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)

𝕏.get_post_api().post_create_tweet(
    tweet_text="Hello World!!",
    media_ids=[str(media.media_id)],
)

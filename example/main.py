import json
import datetime

from pathlib import Path
from tweepy_authlib import CookieSessionUserHandler
from twitter_openapi_python import TwitterOpenapiPython


if Path("cookie.json").exists():
    with open("cookie.json", "r") as f:
        cookies_dict = json.load(f)
else:
    auth_handler = CookieSessionUserHandler(
        screen_name=input("screen_name: "),
        password=input("password: "),
    )
    cookies_dict = auth_handler.get_cookies().get_dict()


𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)

time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
𝕏.get_post_api().post_create_tweet(tweet_text=f"Hello World!!{time}")

response = 𝕏.get_user_api().get_user_by_screen_name("elonmusk")
print(f"rate_limit_remaining: {response.header.rate_limit_remaining}")
elonmusk = response.data.user
print(f"screen_name: {elonmusk.legacy.screen_name}")
print(f"friends_count: {elonmusk.legacy.friends_count}")
print(f"followers_count: {elonmusk.legacy.followers_count}")

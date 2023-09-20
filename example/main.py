import datetime
from twitter_openapi_python import TwitterOpenapiPython

import login

cookies_dict = login.login().get_cookies().get_dict()

𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)

time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
𝕏.get_post_api().post_create_tweet(tweet_text=f"Hello World!!{time}")

response = 𝕏.get_user_api().get_user_by_screen_name("elonmusk")
print(f"rate_limit_remaining: {response.header.rate_limit_remaining}")
elonmusk = response.data.user
print(f"screen_name: {elonmusk.legacy.screen_name}")
print(f"friends_count: {elonmusk.legacy.friends_count}")
print(f"followers_count: {elonmusk.legacy.followers_count}")

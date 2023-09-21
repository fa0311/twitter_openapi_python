from twitter_openapi_python import TwitterOpenapiPython
import login as login


import urllib.request
from urllib.parse import urlparse
import os
from pathlib import Path

cookies_dict = login.login().get_cookies().get_dict()
𝕏 = TwitterOpenapiPython().get_client_from_cookies(cookies=cookies_dict)
screen_name = "elonmusk"
user_response = 𝕏.get_user_api().get_user_by_screen_name(
    screen_name=screen_name,
)

print(f"rate_limit_remaining: {user_response.header.rate_limit_remaining}")
elonmusk = user_response.data.user
print(f"screen_name: {elonmusk.legacy.screen_name}")
print(f"friends_count: {elonmusk.legacy.friends_count}")
print(f"followers_count: {elonmusk.legacy.followers_count}")

os.makedirs("media", exist_ok=True)


url = urlparse(elonmusk.legacy.profile_image_url_https)
ext = os.path.splitext(url.path)[1]
data = urllib.request.urlopen(elonmusk.legacy.profile_image_url_https).read()
os.makedirs("media", exist_ok=True)
with open(Path("media", screen_name + ext), mode="wb+") as f:
    f.write(data)

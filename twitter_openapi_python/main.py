import json
from pathlib import Path
from requests.cookies import RequestsCookieJar
from tweepy_authlib import CookieSessionUserHandler

import twitter_openapi_python as api

# https://github.com/tsukumijima/tweepy-authlib
if Path("cookie.json").exists():
    with open("cookie.json", "r") as f:
        cookies_dict = json.load(f)
    cookies = RequestsCookieJar()
    for key, value in cookies_dict.items():
        cookies.set(key, value)
    auth_handler = CookieSessionUserHandler(cookies=cookies)
else:
    auth_handler = CookieSessionUserHandler(
        screen_name=input("screen_name: "), password=input("password: ")
    )
    cookies = auth_handler.get_cookies()
    with open("cookie.json", "w") as f:
        json.dump(cookies.get_dict(), f, ensure_ascii=False, indent=4)

client = api.TwitterOpenapiPython().get_client_from_cookies(
    ct0=cookies.get_dict()["ct0"],
    authToken=cookies.get_dict()["auth_token"],
)

res = client.get_default_api().get_profile_spotlights_query(screen_name="twitter")
print(res)

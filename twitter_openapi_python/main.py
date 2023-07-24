import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.configuration as twitter_conf
import urllib3
import json
from pathlib import Path
from requests.cookies import RequestsCookieJar
from tweepy_authlib import CookieSessionUserHandler

HASH = "29e05d162f600933fdbf633e992d2d0a249c9413"
PLACEHOLDER = f"https://raw.githubusercontent.com/fa0311/twitter-openapi/{HASH}/src/config/placeholder.json"


# https://github.com/tsukumijima/tweepy-authlib
if Path("cookie.json").exists():
    with open("cookie.json", "r") as f:
        cookies_dict = json.load(f)
    cookies = RequestsCookieJar()
    for key, value in cookies_dict.items():
        cookies.set(key, value)
    auth_handler = CookieSessionUserHandler(cookies=cookies)
else:
    auth_handler = CookieSessionUserHandler(screen_name="", password="")
    cookies = auth_handler.get_cookies()
    with open("cookie.json", "w") as f:
        json.dump(cookies.get_dict(), f, ensure_ascii=False, indent=4)

str_cookie = "; ".join([f"{key}={value}" for key, value in cookies.get_dict().items()])

api_conf = twitter_conf.Configuration(
    api_key={
        "ClientLanguage": "en",
        "ActiveUser": "yes",
        "AuthType": "OAuth2Session",
        # "CookieAuthToken": cookies.get_dict()["auth_token"],
        # "CookieCt0": cookies.get_dict()["ct0"],
        "CsrfToken": cookies.get_dict()["ct0"],
        # "GuestToken": cookies.get_dict()["gt"],
    },
)
api_conf.access_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

api_client = twitter.ApiClient(configuration=api_conf, cookie=str_cookie)
api_client.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
api_instance = twitter.TweetApi(api_client)


http = urllib3.PoolManager()
flag = http.request("GET", PLACEHOLDER).json()

api_instance.get_tweet_detail(
    path_query_id=flag["TweetDetail"]["queryId"],
    variables=json.dumps(flag["TweetDetail"]["variables"]),
    features=json.dumps(flag["TweetDetail"]["features"]),
)

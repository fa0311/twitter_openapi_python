import json
from pathlib import Path
import twitter_openapi_python as api
import logging
from twitter_openapi_python.models.tweet import TweetApiUtilsData


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

import json
import logging
from pathlib import Path

import twitter_openapi_python_generated.models as models

import twitter_openapi_python as api
from twitter_openapi_python.models import TweetApiUtilsData
from twitter_openapi_python.models.timeline import UserApiUtilsData


def get_client() -> api.TwitterOpenapiPythonClient:
    if Path("cookie.json").exists():
        with open("cookie.json", "r") as f:
            cookies_dict = json.load(f)
    else:
        raise Exception("cookie.json not found")

    client = api.TwitterOpenapiPython().get_client_from_cookies(cookies_dict)

    return client


def print_tweet(tweet: TweetApiUtilsData) -> None:
    print_legacy_tweet(tweet.user.legacy, tweet.tweet.legacy)
    for reply in tweet.replies:
        print_legacy_tweet(reply.user.legacy, reply.tweet.legacy)


def print_legacy_tweet(u: models.UserLegacy, t: models.TweetLegacy) -> None:
    text = f"{u.screen_name.rjust(20)}: {t.full_text}"
    logging.info(text.replace("\n", " "))


def print_user(user: UserApiUtilsData) -> None:
    print_legacy_user(user.user.legacy)


def print_legacy_user(u: models.UserLegacy) -> None:
    logging.info(u.screen_name)
    logging.info(f"listedCount: {u.listed_count}")
    logging.info(f"followedBy: {u.followed_by} following: {u.following}")
    text = f"friends_count: {u.friends_count} followers_count: {u.followers_count}"
    logging.info(text)
    logging.info("┄" * 50)

import json
import logging
from pathlib import Path
from typing import Optional

import twitter_openapi_python as api


def get_client() -> api.TwitterOpenapiPythonClient:
    if Path("cookie.json").exists():
        with open("cookie.json", "r") as f:
            cookies_dict = json.load(f)
        if isinstance(cookies_dict, list):
            cookies_dict = {k["name"]: k["value"] for k in cookies_dict}
    else:
        raise Exception("cookie.json not found")

    client = api.TwitterOpenapiPython()
    client.additional_api_headers = {
        "sec-ch-ua-platform": '"Windows"',
    }
    client.additional_browser_headers = {
        "sec-ch-ua-platform": '"Windows"',
    }
    return client.get_client_from_cookies(cookies_dict)


def get_guest_client() -> api.TwitterOpenapiPythonClient:
    client = api.TwitterOpenapiPython().get_guest_client()
    return client


def screen_name(user: api.User) -> str:
    return user.core.screen_name if user.core else str(user.legacy.screen_name)


def print_tweet(tweet: api.TweetApiUtilsData) -> None:
    print_legacy_tweet(tweet.user, tweet.tweet.legacy)
    for reply in tweet.replies:
        print_legacy_tweet(reply.user, reply.tweet.legacy)


def print_legacy_tweet(user: api.User, t: Optional[api.TweetLegacy]) -> None:
    text = f"{screen_name(user).rjust(20)}: {t.full_text if t else 'Deleted Tweet'}"
    logging.info(text.replace("\n", " "))


def print_user(user: api.UserApiUtilsData) -> None:
    print_legacy_user(user.user)


def print_legacy_user(user: api.User) -> None:
    logging.info(screen_name(user))
    if user.relationship_perspectives:
        p = user.relationship_perspectives
        logging.info(f"followedBy: {p.followed_by} following: {p.following}")
    if user.relationship_counts:
        c = user.relationship_counts
        logging.info(f"following: {c.following} followers: {c.followers}")
    logging.info("┄" * 50)

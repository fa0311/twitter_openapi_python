import urllib3
from typing import Any

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.configuration as conf
from twitter_openapi_python.api import (
    DefaultApiUtils,
    PostApiUtils,
    InitialStateApiUtils,
    TweetApiUtils,
    UserApiUtils,
)


class TwitterOpenapiPythonClient:
    api: twitter.ApiClient
    placeholder: dict[str, Any]

    def __init__(self, api: twitter.ApiClient, placeholder: dict[str, Any]):
        self.api = api
        self.placeholder = placeholder

    def get_default_api(self) -> DefaultApiUtils:
        return DefaultApiUtils(twitter.DefaultApi(self.api), self.placeholder)

    def get_initial_state_api(self) -> InitialStateApiUtils:
        return InitialStateApiUtils(self.placeholder)

    def get_post_api(self) -> PostApiUtils:
        return PostApiUtils(twitter.PostApi(self.api), self.placeholder)

    def get_tweet_api(self) -> TweetApiUtils:
        return TweetApiUtils(twitter.TweetApi(self.api), self.placeholder)

    def get_user_api(self) -> UserApiUtils:
        return UserApiUtils(twitter.UserApi(self.api), self.placeholder)


class TwitterOpenapiPython:
    hash: str = "2d477a0fb84d249a30b5af535b467efc25b34923"
    placeholder_url = "https://raw.githubusercontent.com/fa0311/twitter-openapi/{hash}/src/config/placeholder.json"
    placeholder: dict[str, Any]
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    def get_twitter_openapi_python_client(self, api: twitter.ApiClient):
        http = urllib3.PoolManager()
        flag = http.request("GET", self.placeholder_url.format(hash=self.hash)).json()
        return TwitterOpenapiPythonClient(api, flag)

    def get_client(self, api_client: twitter.ApiClient) -> TwitterOpenapiPythonClient:
        return self.get_twitter_openapi_python_client(twitter.TweetApi(api_client))

    def get_client_from_cookies(
        self,
        ct0: str,
        authToken: str,
    ) -> TwitterOpenapiPythonClient:
        api_conf = conf.Configuration(
            api_key={
                "ClientLanguage": "en",
                "ActiveUser": "yes",
                "AuthType": "OAuth2Session",
                # "CookieAuthToken": cookies.get_dict()["auth_token"],
                # "CookieCt0": cookies.get_dict()["ct0"],
                "CsrfToken": ct0,
                # "GuestToken": cookies.get_dict()["gt"],
            },
        )
        cookies = {
            "auth_token": authToken,
            "ct0": ct0,
        }
        api_conf.access_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        str_cookie = "; ".join([f"{key}={value}" for key, value in cookies.items()])
        api_client = twitter.ApiClient(configuration=api_conf, cookie=str_cookie)
        api_client.user_agent = self.user_agent
        return self.get_twitter_openapi_python_client(api_client)

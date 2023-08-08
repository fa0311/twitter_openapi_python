from typing import Any

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.configuration as conf
import urllib3

from twitter_openapi_python.api import V11GetApiUtils  # type: ignore
from twitter_openapi_python.api import V11PostApiUtils  # type: ignore
from twitter_openapi_python.api import V20GetApiUtils  # type: ignore
from twitter_openapi_python.api import (
    DefaultApiUtils,
    InitialStateApiUtils,
    PostApiUtils,
    TweetApiUtils,
    UserApiUtils,
    UserListApiUtils,
    UsersApiUtils,
)

ParamType = dict[str, Any]


class TwitterOpenapiPythonClient:
    api: twitter.ApiClient
    placeholder: ParamType

    def __init__(self, api: twitter.ApiClient, placeholder: ParamType):
        self.api = api
        self.placeholder = placeholder

    def get_default_api(self) -> DefaultApiUtils:
        return DefaultApiUtils(twitter.DefaultApi(self.api), self.placeholder)

    def get_initial_state_api(self) -> InitialStateApiUtils:
        return InitialStateApiUtils(self.api)

    def get_post_api(self) -> PostApiUtils:
        return PostApiUtils(twitter.PostApi(self.api), self.placeholder)

    def get_tweet_api(self) -> TweetApiUtils:
        return TweetApiUtils(twitter.TweetApi(self.api), self.placeholder)

    def get_user_api(self) -> UserApiUtils:
        return UserApiUtils(twitter.UserApi(self.api), self.placeholder)

    def get_users_api(self) -> UsersApiUtils:
        return UsersApiUtils(twitter.UsersApi(self.api), self.placeholder)

    def get_user_list_api(self) -> UserListApiUtils:
        return UserListApiUtils(twitter.UserListApi(self.api), self.placeholder)

    def get_v11_get_api(self) -> V11GetApiUtils:
        return V11GetApiUtils(twitter.V11GetApi(self.api), self.placeholder)

    def get_v11_post_api(self) -> V11PostApiUtils:
        return V11PostApiUtils(twitter.V11PostApi(self.api), self.placeholder)

    def get_v20_get_api(self) -> V20GetApiUtils:
        return V20GetApiUtils(twitter.V20GetApi(self.api), self.placeholder)


class TwitterOpenapiPython:
    hash: str = "2d477a0fb84d249a30b5af535b467efc25b34923"
    placeholder_url = "https://raw.githubusercontent.com/fa0311/twitter-openapi/{hash}/src/config/placeholder.json"
    placeholder: ParamType
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    def get_twitter_openapi_python_client(self, api: twitter.ApiClient):
        http = urllib3.PoolManager()
        flag = http.request("GET", self.placeholder_url.format(hash=self.hash)).json()
        return TwitterOpenapiPythonClient(api, flag)

    def get_client(self, api_client: twitter.ApiClient) -> TwitterOpenapiPythonClient:
        return self.get_twitter_openapi_python_client(api_client)

    def get_client_from_cookies(
        self,
        cookies: dict[str, str],
    ) -> TwitterOpenapiPythonClient:
        api_conf = conf.Configuration(
            api_key={
                "ClientLanguage": "en",
                "ActiveUser": "yes",
                "AuthType": "OAuth2Session",
                "CsrfToken": cookies.get("ct0", ""),
            },
        )
        api_conf.access_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        str_cookie = "; ".join([f"{key}={value}" for key, value in cookies.items()])
        api_client = twitter.ApiClient(configuration=api_conf, cookie=str_cookie)
        api_client.user_agent = self.user_agent
        return self.get_twitter_openapi_python_client(api_client)

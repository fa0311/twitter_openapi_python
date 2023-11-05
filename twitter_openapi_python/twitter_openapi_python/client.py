import json
import re
from typing import Any

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.configuration as conf
import urllib3

from twitter_openapi_python.api import (
    DefaultApiUtils,
    InitialStateApiUtils,
    PostApiUtils,
    TweetApiUtils,
    UserApiUtils,
    UserListApiUtils,
    UsersApiUtils,
    V11GetApiUtils,
    V11PostApiUtils,
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


class TwitterOpenapiPython:
    hash: str = "7560ee63488ec9d15f5389e64867f2413701d7dd"
    placeholder_url = "https://raw.githubusercontent.com/fa0311/twitter-openapi/{hash}/src/config/placeholder.json"
    placeholder: ParamType
    user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    access_token: str = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

    api_key = {
        "Accept": "*/*",
        "AcceptEncoding": "gzip, deflate, br",
        "AcceptLanguage": "en-US,en;q=0.9",
        "CacheControl": "no-cache",
        "Pragma": "no-cache",
        "SecChUa": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "SecChUaMobile": "?0",
        "SecChUaPlatform": '"Windows"',
        "SecFetchDest": "empty",
        "SecFetchMode": "cors",
        "SecFetchSite": "same-origin",
        "ClientLanguage": "en",
        "ActiveUser": "yes",
    }

    browser_headers = {
        "accept": "text/plain, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": user_agent,
    }

    def cookie_normalize(self, cookie: list[str]) -> dict[str, str]:
        return {
            x.split("; ")[0].split("=")[0]: x.split("; ")[0].split("=")[1]
            for x in cookie
        }

    def cookie_to_str(self, cookie: dict[str, str]) -> str:
        return "; ".join([f"{key}={value}" for key, value in cookie.items()])

    def get_twitter_openapi_python_client(
        self,
        api: twitter.ApiClient,
    ) -> TwitterOpenapiPythonClient:
        http = urllib3.PoolManager()
        flag = http.request("GET", self.placeholder_url.format(hash=self.hash)).json()
        return TwitterOpenapiPythonClient(api, flag)

    def get_client_from_cookies(
        self,
        cookies: dict[str, str],
    ) -> TwitterOpenapiPythonClient:
        api_key = self.api_key

        if cookies.get("ct0"):
            api_key.update({"AuthType": "OAuth2Session"})
            api_key.update({"CsrfToken": cookies["ct0"]})

        if cookies.get("gt"):
            api_key.update({"GuestToken": cookies["gt"]})

        api_conf = conf.Configuration(api_key=api_key)
        api_conf.access_token = self.access_token
        api_client = twitter.ApiClient(
            configuration=api_conf,
            cookie=self.cookie_to_str(cookies),
        )
        api_client.user_agent = self.user_agent
        return self.get_twitter_openapi_python_client(api_client)

    def get_guest_client(self) -> TwitterOpenapiPythonClient:
        http = urllib3.PoolManager()
        session = {}

        res_1 = http.request(
            "GET",
            "https://twitter.com",
            redirect=False,
            headers=self.browser_headers,
        )
        cookie = res_1.headers._container["set-cookie"][1:]
        session.update(self.cookie_normalize(cookie))
        res_2 = http.request(
            "GET",
            "https://twitter.com",
            redirect=False,
            headers=self.browser_headers | {"Cookie": self.cookie_to_str(session)},
        )

        find = re.findall(r'document.cookie="(.*?)";', res_2.data.decode())
        session.update(self.cookie_normalize(find))

        session.pop("ct0")

        if not session.get("gt"):
            activate_header = self.browser_headers | {
                "authorization": "Bearer {}".format(self.access_token),
                "x-twitter-active-user": "yes",
                "x-twitter-client-language": "en",
            }
            res_3 = http.request(
                "POST",
                "https://api.twitter.com/1.1/guest/activate.json",
                headers=activate_header | {"Cookie": self.cookie_to_str(session)},
            )
            gt = json.loads(res_3.data.decode())["guest_token"]
            session.update({"gt": gt})

        # ct0 = cookies.get("ct0", "".join(random.choices("0123456789abcdef", k=32)))

        return self.get_client_from_cookies(session)

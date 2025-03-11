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
    hash: str = "a321665475ab77887bd17c2d45dca919eedf10bd"
    placeholder_url = "https://raw.githubusercontent.com/fa0311/twitter-openapi/{hash}/src/config/placeholder.json"
    header = "https://raw.githubusercontent.com/fa0311/latest-user-agent/refs/heads/main/header.json"
    access_token: str = (
        "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    )
    twitter_url: str = "https://x.com/home"
    additional_browser_headers = {}
    additional_api_headers = {}

    def get_header(self) -> tuple[dict[str, str], dict[str, str]]:
        http = urllib3.PoolManager()
        res = http.request("GET", self.header)
        data = json.loads(res.data)
        ignore = ["host", "connection"]

        def getHader(name: str) -> dict[str, str]:
            return {key: value for key, value in data[name].items() if key not in ignore}

        return (
            {
                **getHader("chrome-fetch"),
                "accept-encoding": "identity",
                "referer": self.twitter_url,
                "priority": "u=1, i",
                "x-twitter-client-language": "en",
                "x-twitter-active-user": "yes",
                # 'x-twitter-auth-type': 'xxxx'
                # 'x-csrf-token': 'xxxx',
                # 'x-guest-token': 'xxxx',
                "authorization": f"Bearer {self.access_token}",
                **self.additional_api_headers,
            },
            {
                **getHader("chrome"),
                **self.additional_browser_headers,
            },
        )

    def remove_prefix(self, text: str) -> str:
        if text.startswith("x-twitter-"):
            return text[10:]
        if text.startswith("x-"):
            return text[2:]
        return text

    def kebab_to_upper_camel(self, text: dict[str, Any]) -> dict[str, Any]:
        res = {}
        for key, value in text.items():
            new_key = "".join([x.capitalize() for x in self.remove_prefix(key).split("-")])
            res[new_key] = value
        return res

    def cookie_normalize(self, cookie: list[str]) -> dict[str, str]:
        return {x.split("; ")[0].split("=")[0]: x.split("; ")[0].split("=")[1] for x in cookie}

    def cookie_to_str(self, cookie: dict[str, str]) -> str:
        return "; ".join([f"{key}={value}" for key, value in cookie.items()])

    def get_twitter_openapi_python_client(
        self,
        api: twitter.ApiClient,
    ) -> TwitterOpenapiPythonClient:
        http = urllib3.PoolManager()
        flag = http.request("GET", self.placeholder_url.format(hash=self.hash))
        return TwitterOpenapiPythonClient(api, json.loads(flag.data))

    def get_client_from_cookies(
        self,
        cookies: dict[str, str],
    ) -> TwitterOpenapiPythonClient:
        api_key = self.kebab_to_upper_camel(self.get_header()[0])

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
        api_client.user_agent = api_key["UserAgent"]
        return self.get_twitter_openapi_python_client(api_client)

    def get_guest_client(self) -> TwitterOpenapiPythonClient:
        http = urllib3.PoolManager()
        session = {}

        header = self.get_header()

        res_1 = http.request(
            "GET",
            self.twitter_url,
            redirect=False,
            headers=header[1],
        )
        cookie = res_1.headers._container["set-cookie"][1:]
        session.update(self.cookie_normalize(cookie))
        res_2 = http.request(
            "GET",
            self.twitter_url,
            redirect=False,
            headers=header[1],
        )

        find = re.findall(r'document.cookie="(.*?)";', res_2.data.decode())
        session.update(self.cookie_normalize(find))

        session.pop("ct0")

        if not session.get("gt"):
            activate_header = header[0] | {
                "cookie": self.cookie_to_str(session),
            }
            res_3 = http.request(
                "POST",
                "https://api.x.com/1.1/guest/activate.json",
                headers=activate_header,
            )
            gt = json.loads(res_3.data.decode())["guest_token"]
            session.update({"gt": gt})

        # ct0 = cookies.get("ct0", "".join(random.choices("0123456789abcdef", k=32)))

        return self.get_client_from_cookies(session)

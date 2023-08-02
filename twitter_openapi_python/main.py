import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.configuration as conf
import twitter_openapi_python_generated.models as models
from twitter_openapi_python_generated.api_response import ApiResponse
import urllib3
import json
from pathlib import Path
from requests.cookies import RequestsCookieJar
from tweepy_authlib import CookieSessionUserHandler
from typing import Any, Callable, List, Optional, Type, TypeVar
from twitter_openapi_python.model.timeline import ApiUtilsRaw
from twitter_openapi_python.model.tweet import TweetListApiUtilsResponse

from twitter_openapi_python.utils import (
    buildHeader,
    entriesCursor,
    instructionToEntry,
    tweetEntriesConverter,
)


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
    auth_handler = CookieSessionUserHandler(
        screen_name=input("screen_name: "), password=input("password: ")
    )
    cookies = auth_handler.get_cookies()
    with open("cookie.json", "w") as f:
        json.dump(cookies.get_dict(), f, ensure_ascii=False, indent=4)

str_cookie = "; ".join([f"{key}={value}" for key, value in cookies.get_dict().items()])

api_conf = conf.Configuration(
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

res = api_instance.get_home_timeline(
    path_query_id=flag["HomeTimeline"]["queryId"],
    variables=json.dumps(flag["HomeTimeline"]["variables"]),
    features=json.dumps(flag["HomeTimeline"]["features"]),
)

a = api_instance.get_home_timeline


T = TypeVar("T")


def request(
    apiFn: Callable[[str, str, str], ApiResponse],
    type: Type[T],
    convertFn: Callable[[T], List[models.InstructionUnion]],
    key: str,
    param: dict[str, Any],
) -> TweetListApiUtilsResponse:
    flag = http.request("GET", PLACEHOLDER).json()
    res = apiFn(
        flag[key]["queryId"],
        json.dumps(dict(flag[key]["variables"], **param)),
        json.dumps(flag[key]["features"]),
    )

    if isinstance(res.data.actual_instance, models.Error):
        error: models.Error = res.data.actual_instance
        raise Exception(error)

    instruction = convertFn(res.data.actual_instance)
    entry = instructionToEntry(instruction)
    data = tweetEntriesConverter(entry)

    raw = ApiUtilsRaw(
        response=res,
        instruction=instruction,
        entry=entry,
    )

    return TweetListApiUtilsResponse(
        raw=raw,
        header=buildHeader(res.headers),
        cursor=entriesCursor(entry),
        data=data,
    )


def getHomeTimeline(
    cursor: Optional[str] = None,
    count: Optional[int] = None,
    extraParam: Optional[dict[str, Any]] = None,
):
    param: dict[str, Any] = {}
    if cursor is not None:
        param["cursor"] = cursor
    if count is not None:
        param["count"] = count
    if extraParam is not None:
        param.update(extraParam)

    return request(
        apiFn=api_instance.get_home_timeline_with_http_info,
        type=models.TimelineResponse,
        convertFn=lambda x: x.data.home.home_timeline_urt.instructions,
        key="HomeTimeline",
        param=param,
    )


aa = getHomeTimeline()
print(aa)

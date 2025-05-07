from typing import Any, Callable, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import TweetApiUtilsData, TwitterApiUtilsResponse
from twitter_openapi_python.utils import (
    build_response,
    build_tweet_api_utils,
    get_kwargs,
)
from twitter_openapi_python.utils.api import error_check

T1 = TypeVar("T1")
T2 = TypeVar("T2")
ApiFnType = Callable[..., twitter.ApiResponse[T1]]
ParamType = dict[str, Any]


class DefaultApiUtils:
    api: twitter.DefaultApi
    flag: ParamType

    def __init__(self, api: twitter.DefaultApi, flag: ParamType, ct: ClientTransaction):
        self.api = api
        self.flag = flag
        self.ct = ct

    def request(
        self,
        apiFn: "ApiFnType[T1]",
        convertFn: Callable[[T1], T2],
        key: str,
        param: ParamType,
    ):
        args = get_kwargs(flag=self.flag[key], additional=param, ct=self.ct)
        res = apiFn(**args)
        data = convertFn(res.data)
        return build_response(res, data)

    def get_profile_spotlights_query(
        self,
        screen_name: Optional[str] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.UserResultByScreenName]:
        param: ParamType = {}
        if screen_name is not None:
            param["screen_name"] = screen_name
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_profile_spotlights_query_with_http_info,
            convertFn=lambda x: error_check(x.data.user_result_by_screen_name, x.errors),
            key="ProfileSpotlightsQuery",
            param=param,
        )
        return response

    def get_tweet_result_by_rest_id(
        self,
        tweet_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[TweetApiUtilsData]:
        param: ParamType = {"tweetId": tweet_id}
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_tweet_result_by_rest_id_with_http_info,
            convertFn=lambda x: error_check(
                build_tweet_api_utils(error_check(x.data.tweet_result, x.errors)), x.errors
            ),
            key="TweetResultByRestId",
            param=param,
        )
        if response.data is None:
            raise Exception("No tweet")
        return response  # type: ignore

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from typing import Any, Callable, Optional, Type, TypeVar
import json

from twitter_openapi_python.models.response import (
    TwitterApiUtilsRaw,
    TwitterApiUtilsResponse,
)
from twitter_openapi_python.utils.api import build_header


T1 = TypeVar("T1")
T2 = TypeVar("T2")


class DefaultApiUtils:
    api: twitter.DefaultApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.DefaultApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: Callable[[str, str, str], twitter.ApiResponse],
        convertFn: Callable[[T1], T2],
        type1: Type[T1],
        type2: Type[T2],
        key: str,
        param: dict[str, Any],
    ) -> TwitterApiUtilsResponse[T2]:
        res = apiFn(
            self.flag[key]["queryId"],
            json.dumps(self.flag[key]["variables"] | param),
            json.dumps(self.flag[key]["features"]),
        )
        if isinstance(res.data.actual_instance, models.Error):
            error: models.Error = res.data.actual_instance
            raise Exception(error)

        data = convertFn(res.data.actual_instance)

        return TwitterApiUtilsResponse(
            raw=TwitterApiUtilsRaw(response=res),
            header=build_header(res.headers),
            data=data,
        )

    def get_profile_spotlights_query(
        self,
        screen_name: Optional[str] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> TwitterApiUtilsResponse[models.UserResultByScreenName]:
        param: dict[str, Any] = {}
        if screen_name is not None:
            param["screen_name"] = screen_name
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_profile_spotlights_query_with_http_info,
            convertFn=lambda x: x.data.user_result_by_screen_name,
            type1=models.ProfileResponse,
            type2=models.UserResultByScreenName,
            key="ProfileSpotlightsQuery",
            param=param,
        )
        return response

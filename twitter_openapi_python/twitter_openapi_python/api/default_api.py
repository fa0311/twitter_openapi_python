import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from twitter_openapi_python_generated.api_response import ApiResponse
from typing import Any, Callable, Optional, Type, TypeVar
import json


T = TypeVar("T")


class DefaultApiUtils:
    api: twitter.DefaultApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.DefaultApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: Callable[[str, str, str], ApiResponse],
        type: Type[T],
        key: str,
        param: dict[str, Any],
    ) -> T:
        res = apiFn(
            self.flag[key]["queryId"],
            json.dumps(self.flag[key]["variables"] | param),
            json.dumps(self.flag[key]["features"]),
        )
        if isinstance(res.data.actual_instance, models.Error):
            error: models.Error = res.data.actual_instance
            raise Exception(error)
        return res.data.actual_instance

    def get_profile_spotlights_query(
        self,
        screen_name: Optional[str] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> models.UserResultByScreenName:
        param: dict[str, Any] = {}
        if screen_name is not None:
            param["screen_name"] = screen_name
        if extra_param is not None:
            param.update(extra_param)

        return self.request(
            apiFn=self.api.get_profile_spotlights_query_with_http_info,
            type=models.ProfileResponse,
            key="ProfileSpotlightsQuery",
            param=param,
        )

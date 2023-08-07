import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from typing import Any, Callable, Optional, Type, TypeVar

from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.utils.api import build_response, check_error, get_kwargs


T1 = TypeVar("T1")
T2 = TypeVar("T2")
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class DefaultApiUtils:
    api: twitter.DefaultApi
    flag: ParamType

    def __init__(self, api: twitter.DefaultApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T1], T2],
        type1: Type[T1],
        type2: Type[T2],
        key: str,
        param: ParamType,
    ) -> TwitterApiUtilsResponse[T2]:
        args = get_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(**args)
        checked = check_error(data=res, type=type1)

        data = convertFn(checked)

        return build_response(response=res, data=data)

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
            convertFn=lambda x: x.data.user_result_by_screen_name,
            type1=models.ProfileResponse,
            type2=models.UserResultByScreenName,
            key="ProfileSpotlightsQuery",
            param=param,
        )
        return response

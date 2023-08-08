from types import NoneType
from typing import Any, Callable, Optional, Type, TypeVar

import twitter_openapi_python_generated as twitter

from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.utils.api import build_response, get_legacy_kwargs

T = TypeVar("T")
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class V11PostApiUtils:
    api: twitter.V11PostApi
    flag: ParamType

    def __init__(self, api: twitter.V11PostApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        type: Type[T],
        key: str,
        param: ParamType,
    ) -> TwitterApiUtilsResponse[T]:
        args = get_legacy_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(**args)
        data = res.data

        if not isinstance(data, type):
            raise Exception("Error")

        return build_response(response=res, data=data)

    def post_create_friendships(
        self,
        user_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[None]:
        param = {"user_id": user_id}
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.post_create_friendships_with_http_info,
            type=NoneType,
            param=param,
            key="friendships/create.json",
        )
        return response

    def post_destroy_friendships(
        self,
        user_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[None]:
        param = {"user_id": user_id}
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.post_destroy_friendships_with_http_info,
            type=NoneType,
            param=param,
            key="friendships/destroy.json",
        )
        return response

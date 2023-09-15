from types import NoneType
from typing import Any, Callable, Optional, Type, TypeVar

import twitter_openapi_python_generated as twitter

from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.utils import build_response, get_legacy_kwargs

T = TypeVar("T")
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class V11GetApiUtils:
    api: twitter.V11GetApi
    flag: ParamType

    def __init__(self, api: twitter.V11GetApi, flag: ParamType):
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

    def get_friends_following_list(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[None]:
        param: ParamType = {"user_id": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_friends_following_list_with_http_info,
            type=NoneType,
            param=param,
            key="friends/following/list.json",
        )
        return response

    def get_search_typeahead(
        self,
        q: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[None]:
        param = {"q": q}
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_search_typeahead_with_http_info,
            type=NoneType,
            param=param,
            key="search/typeahead.json",
        )
        return response

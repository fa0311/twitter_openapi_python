import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from twitter_openapi_python.models import TwitterApiUtilsResponse, ApiUtilsHeader
from twitter_openapi_python.models.timeline import UserApiUtilsData
from twitter_openapi_python.utils.api import (
    build_response,
    get_kwargs,
    user_result_converter,
    check_error,
)
from typing import Any, Callable, Type, TypeVar, Optional, Union

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[list[UserApiUtilsData], ApiUtilsHeader]


ApiFnType = Union[
    Callable[[str, str, str], twitter.ApiResponse],
    Callable[[str, str, str, str], twitter.ApiResponse],
]


class UsersApiUtils:
    api: twitter.UsersApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.UsersApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T], list[models.UserResults]],
        type: Type[T],
        key: str,
        param: dict[str, Any],
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(*args.values())
        checked = check_error(data=res, type=type)

        user_result = convertFn(checked)
        user = user_result_converter(user_result)
        return build_response(
            response=res,
            data=user,
            type=ApiUtilsHeader,
        )

    def get_users_by_rest_ids(
        self,
        user_ids: list[str],
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "userIds": user_ids,
        }
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_users_by_rest_ids_with_http_info,
            convertFn=lambda e: e.data.users,
            type=models.UsersResponse,
            key="UsersByRestIds",
            param=param,
        )

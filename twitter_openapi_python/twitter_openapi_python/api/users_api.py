from typing import Any, Callable, Optional, Type, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.models import TwitterApiUtilsResponse, UserApiUtilsData
from twitter_openapi_python.utils import (
    build_response,
    check_error,
    get_kwargs,
    user_result_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[list[UserApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class UsersApiUtils:
    api: twitter.UsersApi
    flag: ParamType

    def __init__(self, api: twitter.UsersApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T], list[models.UserResults]],
        type: Type[T],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(**args)
        checked = check_error(data=res, type=type)

        user_result = convertFn(checked)
        user = user_result_converter(user_result)
        return build_response(response=res, data=user)

    def get_users_by_rest_ids(
        self,
        user_ids: list[str],
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userIds": user_ids}
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_users_by_rest_ids_with_http_info,
            convertFn=lambda e: e.data.users,
            type=models.UsersResponse,
            key="UsersByRestIds",
            param=param,
        )

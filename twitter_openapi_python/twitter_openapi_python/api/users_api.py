from typing import Any, Callable, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import TwitterApiUtilsResponse, UserApiUtilsData
from twitter_openapi_python.utils import (
    build_response,
    error_check,
    get_kwargs,
    user_result_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[list[UserApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class UsersApiUtils:
    api: twitter.UsersApi
    flag: ParamType

    def __init__(self, api: twitter.UsersApi, flag: ParamType, ct: ClientTransaction):
        self.api = api
        self.flag = flag
        self.ct = ct

    def request(
        self,
        apiFn: "ApiFnType[T]",
        convertFn: Callable[[T], list[models.UserResults]],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param, ct=self.ct)
        res = apiFn(**args)
        user_result = convertFn(res.data)
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
            convertFn=lambda e: error_check(e.data.users, e.errors),
            key="UsersByRestIds",
            param=param,
        )

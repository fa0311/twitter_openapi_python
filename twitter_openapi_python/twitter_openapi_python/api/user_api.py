from typing import Any, Callable, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import TwitterApiUtilsResponse, UserApiUtilsData
from twitter_openapi_python.utils import (
    build_response,
    error_check,
    get_kwargs,
    user_or_null_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[UserApiUtilsData]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class UserApiUtils:
    api: twitter.UserApi
    flag: ParamType

    def __init__(self, api: twitter.UserApi, flag: ParamType, ct: ClientTransaction):
        self.api = api
        self.flag = flag
        self.ct = ct

    def request(
        self,
        apiFn: "ApiFnType[T]",
        convertFn: Callable[[T], models.UserResults],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param, ct=self.ct)
        res = apiFn(**args)
        result = convertFn(res.data)
        if result.result is None:
            raise Exception("No user")
        user = user_or_null_converter(result.result)
        if user is None:
            raise Exception("No user")
        data = UserApiUtilsData(
            raw=result,
            user=user,
        )

        return build_response(response=res, data=data)

    def get_user_by_screen_name(
        self,
        screen_name: str,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"screen_name": screen_name}
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_screen_name_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors),
            key="UserByScreenName",
            param=param,
        )

    def get_user_by_rest_id(
        self,
        user_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_rest_id_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors),
            key="UserByRestId",
            param=param,
        )

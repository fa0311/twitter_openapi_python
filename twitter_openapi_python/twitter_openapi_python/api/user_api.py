import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from twitter_openapi_python.models import (
    TwitterApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils.api import (
    build_response,
    check_error,
    get_kwargs,
    user_or_null_converter,
)
from typing import Any, Callable, Type, TypeVar, Optional

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[UserApiUtilsData]


ApiFnType = Callable[..., twitter.ApiResponse]


class UserApiUtils:
    api: twitter.UserApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.UserApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T], models.UserResults],
        type: Type[T],
        key: str,
        param: dict[str, Any],
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(*args.values())
        checked = check_error(data=res, type=type)

        result = convertFn(checked)
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
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "screen_name": screen_name,
        }
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_screen_name_with_http_info,
            convertFn=lambda e: e.data.user,
            type=models.UserResponse,
            key="UserByScreenName",
            param=param,
        )

    def get_user_by_rest_id(
        self,
        user_id: str,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "userId": user_id,
        }
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_rest_id_with_http_info,
            convertFn=lambda e: e.data.user,
            type=models.UserResponse,
            key="UserByRestId",
            param=param,
        )

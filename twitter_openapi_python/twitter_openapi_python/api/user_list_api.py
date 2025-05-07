from typing import Any, Callable, List, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import (
    ApiUtilsRaw,
    TimelineApiUtilsResponse,
    TwitterApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils import (
    build_response,
    entries_cursor,
    error_check,
    get_kwargs,
    instruction_to_entry,
    user_entries_converter,
    user_result_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[UserApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class UserListApiUtils:
    api: twitter.UserListApi
    flag: ParamType

    def __init__(self, api: twitter.UserListApi, flag: ParamType, ct: ClientTransaction):
        self.api = api
        self.flag = flag
        self.ct = ct

    def request(
        self,
        apiFn: "ApiFnType[T]",
        convertFn: Callable[[T], List[models.InstructionUnion]],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param, ct=self.ct)
        res = apiFn(**args)
        instruction = convertFn(res.data)
        entry = instruction_to_entry(instruction)
        user_list = user_entries_converter(entry)
        user = user_result_converter(user_list)

        raw = ApiUtilsRaw(
            instruction=instruction,
            entry=entry,
        )
        data = TimelineApiUtilsResponse[UserApiUtilsData](
            raw=raw,
            cursor=entries_cursor(entry),
            data=user,
        )

        return build_response(response=res, data=data)

    def get_followers(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_followers_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors).result.timeline.timeline.instructions,
            key="Followers",
            param=param,
        )

    def get_following(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_following_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors).result.timeline.timeline.instructions,
            key="Following",
            param=param,
        )

    def get_followers_you_know(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_followers_you_know_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors).result.timeline.timeline.instructions,
            key="FollowersYouKnow",
            param=param,
        )

    def get_favoriters(
        self,
        tweet_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"tweetId": tweet_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_favoriters_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.favoriters_timeline, e.errors).timeline, e.errors
            ).instructions,
            key="Favoriters",
            param=param,
        )

    def get_retweeters(
        self,
        tweet_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"tweetId": tweet_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_retweeters_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.retweeters_timeline, e.errors).timeline, e.errors
            ).instructions,
            key="Retweeters",
            param=param,
        )

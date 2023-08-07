import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.models.timeline import (
    ApiUtilsRaw,
    TimelineApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils.api import (
    build_response,
    check_error,
    entries_cursor,
    get_kwargs,
    instruction_to_entry,
    user_entries_converter,
    user_result_converter,
)
from typing import Any, Callable, Type, TypeVar, Optional, List

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[UserApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class UserListApiUtils:
    api: twitter.UserListApi
    flag: ParamType

    def __init__(self, api: twitter.UserListApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T], List[models.InstructionUnion]],
        type: Type[T],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(**args)
        checked = check_error(data=res, type=type)

        instruction = convertFn(checked)
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
            convertFn=lambda e: e.data.user.result.timeline.timeline.instructions,
            type=models.FollowResponse,
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
            convertFn=lambda e: e.data.user.result.timeline.timeline.instructions,
            type=models.FollowResponse,
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
            convertFn=lambda e: e.data.user.result.timeline.timeline.instructions,
            type=models.FollowResponse,
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
            convertFn=lambda e: e.data.favoriters_timeline.timeline.instructions,
            type=models.TweetFavoritersResponse,
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
            convertFn=lambda e: e.data.retweeters_timeline.timeline.instructions,
            type=models.TweetRetweetersResponse,
            key="Retweeters",
            param=param,
        )

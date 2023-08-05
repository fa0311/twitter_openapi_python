import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from twitter_openapi_python.models import TwitterApiUtilsResponse, ApiUtilsHeader
from twitter_openapi_python.models.timeline import (
    ApiUtilsRaw,
    TimelineApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils.api import (
    build_response,
    build_user_response,
    entries_cursor,
    instruction_to_entry,
    user_entries_converter,
)
from typing import Any, Callable, Type, TypeVar, Optional, List
import json

T = TypeVar("T")


ResponseType = TwitterApiUtilsResponse[
    TimelineApiUtilsResponse[UserApiUtilsData],
    ApiUtilsHeader,
]


class UserListApiUtils:
    api: twitter.UserListApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.UserListApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: Callable[[str, str, str], twitter.ApiResponse],
        convertFn: Callable[[T], List[models.InstructionUnion]],
        type: Type[T],
        key: str,
        param: dict[str, Any],
    ) -> ResponseType:
        assert key in self.flag.keys()

        kwargs = {
            "path_query_id": self.flag[key]["queryId"],
            "variables": json.dumps(self.flag[key]["variables"] | param),
            "features": json.dumps(self.flag[key]["features"]),
        }
        if "fieldToggles" in self.flag[key].keys():
            kwargs["field_toggles"] = json.dumps(self.flag[key]["fieldToggles"])

        res = apiFn(**kwargs)
        if isinstance(res.data.actual_instance, models.Errors):
            errors: models.Errors = res.data.actual_instance
            raise Exception(errors)
        instruction = convertFn(res.data.actual_instance)
        entry = instruction_to_entry(instruction)
        user_list = user_entries_converter(entry)

        user = list(map(lambda x: build_user_response(x), user_list))

        raw = ApiUtilsRaw(
            instruction=instruction,
            entry=entry,
        )
        data = TimelineApiUtilsResponse[UserApiUtilsData](
            raw=raw,
            cursor=entries_cursor(entry),
            data=user,
        )

        return build_response(
            response=res,
            data=data,
            type=ApiUtilsHeader,
        )

    def get_followers(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "userId": user_id,
        }
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
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "userId": user_id,
        }
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
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "userId": user_id,
        }
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
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "tweetId": tweet_id,
        }
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
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "tweetId": tweet_id,
        }
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

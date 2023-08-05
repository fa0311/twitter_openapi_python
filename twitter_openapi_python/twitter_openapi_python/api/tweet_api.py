import twitter_openapi_python_generated as twitter

import twitter_openapi_python_generated.models as models
from twitter_openapi_python.models import (
    ApiUtilsRaw,
    TwitterApiUtilsResponse,
    TimelineApiUtilsResponse,
)
from twitter_openapi_python.models import ApiUtilsHeader
from twitter_openapi_python.models import TweetApiUtilsData

from twitter_openapi_python.utils.api import (
    instruction_to_entry,
    tweet_entries_converter,
    entries_cursor,
    build_response,
)

from typing import Any, Callable, Type, TypeVar, List, Optional, Union
import json


T = TypeVar("T")

ResponseType = TwitterApiUtilsResponse[
    TimelineApiUtilsResponse[TweetApiUtilsData],
    ApiUtilsHeader,
]

ApiFnType = Union[
    Callable[[str, str, str], twitter.ApiResponse],
    Callable[[str, str, str, str], twitter.ApiResponse],
]


class TweetApiUtils:
    api: twitter.TweetApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.TweetApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: ApiFnType,
        convertFn: Callable[[T], List[models.InstructionUnion]],
        type: Type[T],
        key: str,
        param: dict[str, Any],
    ) -> ResponseType:
        assert key in self.flag.keys()

        args: list[str] = [
            self.flag[key]["queryId"],
            json.dumps(self.flag[key]["variables"] | param),
            json.dumps(self.flag[key]["features"]),
        ]

        if "fieldToggles" in self.flag[key].keys():
            args.append(json.dumps(self.flag[key]["fieldToggles"]))

        res = apiFn(*args)
        if res.data is None:
            raise Exception("No data")
        if isinstance(res.data.actual_instance, models.Errors):
            errors: models.Errors = res.data.actual_instance
            raise Exception(errors)
        instruction = convertFn(res.data.actual_instance)
        entry = instruction_to_entry(instruction)
        tweet_list = tweet_entries_converter(entry)
        raw = ApiUtilsRaw(
            instruction=instruction,
            entry=entry,
        )
        data = TimelineApiUtilsResponse[TweetApiUtilsData](
            raw=raw,
            cursor=entries_cursor(entry),
            data=tweet_list,
        )

        return build_response(
            response=res,
            data=data,
            type=ApiUtilsHeader,
        )

    def get_tweet_detail(
        self,
        focal_tweet_id: str,
        cursor: Optional[str] = None,
        controller_data: Optional[str] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "focalTweetId": focal_tweet_id,
        }
        if cursor is not None:
            param["cursor"] = cursor
        if controller_data is not None:
            param["controller_data"] = controller_data
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_tweet_detail_with_http_info,
            convertFn=lambda e: e.data.threaded_conversation_with_injections_v2.instructions,
            type=models.TweetDetailResponse,
            key="TweetDetail",
            param=param,
        )
        return response

    def get_search_timeline(
        self,
        raw_query: str,
        product: Optional[str] = None,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "rawQuery": raw_query,
        }
        if product is not None:
            param["product"] = product
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_search_timeline_with_http_info,
            convertFn=lambda e: e.data.search_by_raw_query.search_timeline.timeline.instructions,
            type=models.SearchTimelineResponse,
            key="SearchTimeline",
            param=param,
        )
        return response

    def get_home_timeline(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_home_timeline_with_http_info,
            convertFn=lambda e: e.data.home.home_timeline_urt.instructions,
            type=models.TimelineResponse,
            key="HomeTimeline",
            param=param,
        )
        return response

    def get_home_latest_timeline(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_home_latest_timeline_with_http_info,
            convertFn=lambda e: e.data.home.home_timeline_urt.instructions,
            type=models.TimelineResponse,
            key="HomeLatestTimeline",
            param=param,
        )
        return response

    def get_list_latest_tweets_timeline(
        self,
        list_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {
            "listId": list_id,
        }
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_list_latest_tweets_timeline_with_http_info,
            convertFn=lambda e: e.data.list.tweets_timeline.timeline.instructions,
            type=models.ListLatestTweetsTimelineResponse,
            key="ListLatestTweetsTimeline",
            param=param,
        )
        return response

    def get_user_tweets(
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

        response = self.request(
            apiFn=self.api.get_user_tweets_with_http_info,
            convertFn=lambda e: e.data.user.result.timeline_v2.timeline.instructions,
            type=models.UserTweetsResponse,
            key="UserTweets",
            param=param,
        )
        return response

    def get_user_tweets_and_replies(
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

        response = self.request(
            apiFn=self.api.get_user_tweets_and_replies_with_http_info,
            convertFn=lambda e: e.data.user.result.timeline_v2.timeline.instructions,
            type=models.UserTweetsResponse,
            key="UserTweetsAndReplies",
            param=param,
        )
        return response

    def get_user_media(
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

        response = self.request(
            apiFn=self.api.get_user_media_with_http_info,
            convertFn=lambda e: e.data.user.result.timeline_v2.timeline.instructions,
            type=models.UserTweetsResponse,
            key="UserMedia",
            param=param,
        )
        return response

    def get_likes(
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

        response = self.request(
            apiFn=self.api.get_likes_with_http_info,
            convertFn=lambda e: e.data.user.result.timeline_v2.timeline.instructions,
            type=models.UserTweetsResponse,
            key="Likes",
            param=param,
        )
        return response

    def get_bookmarks(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[dict[str, Any]] = None,
    ) -> ResponseType:
        param: dict[str, Any] = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_bookmarks_with_http_info,
            convertFn=lambda e: e.data.bookmark_timeline_v2.timeline.instructions,
            type=models.BookmarksResponse,
            key="Bookmarks",
            param=param,
        )
        return response

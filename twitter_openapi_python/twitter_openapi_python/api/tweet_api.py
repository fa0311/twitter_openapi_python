from typing import Any, Callable, List, Optional, Type, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.models import (
    ApiUtilsRaw,
    TimelineApiUtilsResponse,
    TweetApiUtilsData,
    TwitterApiUtilsResponse,
)
from twitter_openapi_python.utils.api import (
    build_response,
    check_error,
    entries_cursor,
    get_kwargs,
    instruction_to_entry,
    tweet_entries_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[TweetApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse]
ParamType = dict[str, Any]


class TweetApiUtils:
    api: twitter.TweetApi
    flag: ParamType

    def __init__(self, api: twitter.TweetApi, flag: ParamType):
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

        return build_response(response=res, data=data)

    def get_tweet_detail(
        self,
        focal_tweet_id: str,
        cursor: Optional[str] = None,
        controller_data: Optional[str] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"focalTweetId": focal_tweet_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"rawQuery": raw_query}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"listId": list_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"userId": user_id}
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {}
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

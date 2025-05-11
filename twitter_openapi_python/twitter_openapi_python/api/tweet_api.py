from typing import Any, Callable, List, Literal, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import (
    ApiUtilsRaw,
    TimelineApiUtilsResponse,
    TweetApiUtilsData,
    TwitterApiUtilsResponse,
)
from twitter_openapi_python.utils import (
    build_response,
    entries_cursor,
    error_check,
    get_kwargs,
    instruction_to_entry,
    tweet_entries_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[TweetApiUtilsData]]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class TweetApiUtils:
    api: twitter.TweetApi
    flag: ParamType

    def __init__(self, api: twitter.TweetApi, flag: ParamType, ct: ClientTransaction):
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
        return build_response(res, data)

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
            convertFn=lambda e: error_check(e.data.threaded_conversation_with_injections_v2, e.errors).instructions,
            key="TweetDetail",
            param=param,
        )
        return response

    def get_search_timeline(
        self,
        raw_query: str,
        product: Optional[Literal["Top", "Latest", "People", "Photos", "Videos"]] = None,
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
            convertFn=lambda e: error_check(e.data.search_by_raw_query, e.errors).search_timeline.timeline.instructions,
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
            convertFn=lambda e: error_check(e.data.home, e.errors).home_timeline_urt.instructions,
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
            convertFn=lambda e: error_check(e.data.home, e.errors).home_timeline_urt.instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data.list, e.errors).tweets_timeline.timeline, e.errors
            ).instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
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
            convertFn=lambda e: error_check(
                error_check(e.data, e.errors).bookmark_timeline_v2.timeline, e.errors
            ).instructions,
            key="Bookmarks",
            param=param,
        )
        return response

    def get_community_tweets_timeline(
        self,
        communityId: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        rankingMode: Optional[Literal["Recency", "Relevance"]] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"communityId": communityId}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if rankingMode is not None:
            param["rankingMode"] = rankingMode
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_community_tweets_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data, e.errors).community_results.result.ranked_community_timeline.timeline, e.errors
            ).instructions,
            key="CommunityTweetsTimeline",
            param=param,
        )
        return response

    def get_community_media_timeline(
        self,
        communityId: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"communityId": communityId}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_community_media_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data, e.errors).community_results.result.community_media_timeline.timeline, e.errors
            ).instructions,
            key="CommunityMediaTimeline",
            param=param,
        )
        return response

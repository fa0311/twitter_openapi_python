from typing import Any, Callable, List, Literal, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import (
    CommunityApiUtilsData,
    TimelineApiUtilsResponse,
    TweetApiUtilsData,
    TwitterApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils import (
    community_entries_converter,
    error_check,
    notification_entries_converter,
    timeline_request,
    trend_entries_converter,
    tweet_entries_converter,
    user_entries_converter,
    user_result_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[TweetApiUtilsData]]
UserResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[UserApiUtilsData]]
TrendResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[models.TimelineTrend]]
NotificationResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[models.TimelineNotification]]
CommunityResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[CommunityApiUtilsData]]
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
        return timeline_request(apiFn, self.flag[key], self.ct, convertFn, param, tweet_entries_converter)

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

    def get_user_originals_timeline(
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
            apiFn=self.api.get_user_originals_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
            key="UserOriginalsTimeline",
            param=param,
        )
        return response

    def get_user_replies_timeline(
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
            apiFn=self.api.get_user_replies_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
            key="UserRepliesTimeline",
            param=param,
        )
        return response

    def get_user_video_timeline(
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
            apiFn=self.api.get_user_video_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
            key="UserVideoTimeline",
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
        community_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        rankingMode: Optional[Literal["Recency", "Relevance"]] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"communityId": community_id}
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
        community_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"communityId": community_id}
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

    def get_user_highlights_tweets(
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
            apiFn=self.api.get_user_highlights_tweets_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors).result.timeline.timeline.instructions,
            key="UserHighlightsTweets",
            param=param,
        )
        return response

    def get_user_reposts_timeline(
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
            apiFn=self.api.get_user_reposts_timeline_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
            key="UserRepostsTimeline",
            param=param,
        )
        return response

    def get_user_super_follow_tweets(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Subscriber-only posts; without a subscription the timeline only carries a TimelineMessagePrompt."""
        param: ParamType = {"userId": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.get_user_super_follow_tweets_with_http_info,
            convertFn=lambda e: error_check(
                error_check(e.data.user, e.errors).result.timeline.timeline, e.errors
            ).instructions,
            key="UserSuperFollowTweets",
            param=param,
        )
        return response

    def get_explore_page(
        self,
        cursor: Optional[str] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TrendResponseType:
        """Trends of the first explore tab; the other tabs are GenericTimelineById timelines."""
        param: ParamType = {}
        if cursor is not None:
            param["cursor"] = cursor
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_explore_page_with_http_info,
            self.flag["ExplorePage"],
            self.ct,
            lambda e: error_check(e.data.explore_page.body.initial_timeline.timeline.timeline, e.errors).instructions,
            param,
            trend_entries_converter,
        )

    def get_generic_timeline_by_id(
        self,
        timeline_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TrendResponseType:
        """Explore tab timelines (trending, news, sports, ...)."""
        param: ParamType = {"timelineId": timeline_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_generic_timeline_by_id_with_http_info,
            self.flag["GenericTimelineById"],
            self.ct,
            lambda e: error_check(e.data.timeline.timeline, e.errors).instructions,
            param,
            trend_entries_converter,
        )

    def get_notifications_timeline(
        self,
        timeline_type: Optional[Literal["All", "Verified", "Mentions"]] = None,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> NotificationResponseType:
        """Notification items only; the tweets of the Mentions tab are in data.raw.entry (tweet_entries_converter)."""
        param: ParamType = {}
        if timeline_type is not None:
            param["timeline_type"] = timeline_type
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_notifications_timeline_with_http_info,
            self.flag["NotificationsTimeline"],
            self.ct,
            lambda e: error_check(
                e.data.viewer_v2.user_results.result.notification_timeline.timeline, e.errors
            ).instructions,
            param,
            notification_entries_converter,
        )

    def get_community_discovery_timeline(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> CommunityResponseType:
        param: ParamType = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_community_discovery_timeline_with_http_info,
            self.flag["CommunityDiscoveryTimeline"],
            self.ct,
            lambda e: error_check(e.data.viewer.community_discovery_timeline.timeline, e.errors).instructions,
            param,
            community_entries_converter,
        )

    def get_community_about_timeline(
        self,
        community_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> UserResponseType:
        """Moderators and members of a community."""
        param: ParamType = {"communityId": community_id}
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_community_about_timeline_with_http_info,
            self.flag["CommunityAboutTimeline"],
            self.ct,
            lambda e: error_check(e.data.community_results.result.about_timeline.timeline, e.errors).instructions,
            param,
            lambda entry: user_result_converter(user_entries_converter(entry)),
        )

    def get_connect_tab_timeline(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> UserResponseType:
        """Who to follow."""
        param: ParamType = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)

        return timeline_request(
            self.api.get_connect_tab_timeline_with_http_info,
            self.flag["ConnectTabTimeline"],
            self.ct,
            lambda e: error_check(e.data.connect_tab_timeline.timeline, e.errors).instructions,
            param,
            lambda entry: user_result_converter(user_entries_converter(entry)),
        )

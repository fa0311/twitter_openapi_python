from typing import Any, List, Optional

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import (
    TimelineApiUtilsResponse,
    TweetApiUtilsData,
    TwitterApiUtilsResponse,
)
from twitter_openapi_python.utils import (
    data_request,
    error_check,
    timeline_request,
    tweet_entries_converter,
)

ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[TweetApiUtilsData]]
ParamType = dict[str, Any]


class CommunityApiUtils:
    api: twitter.CommunityApi
    flag: ParamType

    def __init__(self, api: twitter.CommunityApi, flag: ParamType, ct: Optional[ClientTransaction]):
        self.api = api
        self.flag = flag
        self.ct = ct

    def get_communities_fetch_one_query(
        self,
        community_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.CommunityPageCommunity]:
        """The community page (full members and moderators)."""
        param: ParamType = {"communityId": community_id}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_communities_fetch_one_query_with_http_info,
            self.flag["CommunitiesFetchOneQuery"],
            self.ct,
            lambda e: error_check(e.data, e.errors).community_results.result,
            param,
        )

    def get_community_query(
        self,
        community_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.CommunitySettingsCommunity]:
        """The community settings / moderation pages (partial users, trending hashtags)."""
        param: ParamType = {"communityId": community_id}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_community_query_with_http_info,
            self.flag["CommunityQuery"],
            self.ct,
            lambda e: error_check(e.data, e.errors).community_results.result,
            param,
        )

    def get_communities_search_query(
        self,
        query: str,
        cursor: Optional[str] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.CommunitiesSearchSlice]:
        """Community cards for a query; the next page is slice_info.next_cursor."""
        param: ParamType = {"query": query}
        if cursor is not None:
            param["cursor"] = cursor
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_communities_search_query_with_http_info,
            self.flag["CommunitiesSearchQuery"],
            self.ct,
            lambda e: error_check(e.data, e.errors).communities_search_slice,
            param,
        )

    def get_topic_carousel_query(
        self,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[List[models.CommunityTopic]]:
        param: ParamType = {}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_topic_carousel_query_with_http_info,
            self.flag["TopicCarouselQuery"],
            self.ct,
            lambda e: error_check(e.data, e.errors).community_topic_results.community_topics,
            param,
        )

    def get_global_communities_post_search_timeline(
        self,
        raw_query: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Posts across communities (Top)."""
        param: ParamType = {"rawQuery": raw_query}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_global_communities_post_search_timeline_with_http_info,
            self.flag["GlobalCommunitiesPostSearchTimeline"],
            self.ct,
            lambda e: error_check(e.data.search_by_raw_query.communities_posts_search_page.timeline, e.errors).instructions,
            param,
            tweet_entries_converter,
        )

    def get_global_communities_latest_post_search_timeline(
        self,
        raw_query: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Posts across communities (Latest)."""
        param: ParamType = {"rawQuery": raw_query}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_global_communities_latest_post_search_timeline_with_http_info,
            self.flag["GlobalCommunitiesLatestPostSearchTimeline"],
            self.ct,
            lambda e: error_check(
                e.data.search_by_raw_query.communities_latest_posts_search_page.timeline, e.errors
            ).instructions,
            param,
            tweet_entries_converter,
        )

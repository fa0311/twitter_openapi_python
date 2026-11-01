from typing import Any, Callable, List, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import (
    TimelineApiUtilsResponse,
    TwitterApiUtilsResponse,
    UserApiUtilsData,
)
from twitter_openapi_python.utils import (
    data_request,
    error_check,
    list_entries_converter,
    timeline_request,
    user_entries_converter,
    user_result_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[UserApiUtilsData]]
ListResponseType = TwitterApiUtilsResponse[TimelineApiUtilsResponse[models.TwitterList]]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class UserListApiUtils:
    api: twitter.UserListApi
    flag: ParamType

    def __init__(self, api: twitter.UserListApi, flag: ParamType, ct: Optional[ClientTransaction]):
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
        return timeline_request(
            apiFn,
            self.flag[key],
            self.ct,
            convertFn,
            param,
            lambda entry: user_result_converter(user_entries_converter(entry)),
        )

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
            convertFn=lambda e: (
                error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline.instructions
            ),
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
            convertFn=lambda e: (
                error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline.instructions
            ),
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
            convertFn=lambda e: (
                error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline.instructions
            ),
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
            convertFn=lambda e: (
                error_check(error_check(e.data.favoriters_timeline, e.errors).timeline, e.errors).instructions
            ),
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
            convertFn=lambda e: (
                error_check(error_check(e.data.retweeters_timeline, e.errors).timeline, e.errors).instructions
            ),
            key="Retweeters",
            param=param,
        )

    def get_blue_verified_followers(
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
            apiFn=self.api.get_blue_verified_followers_with_http_info,
            convertFn=lambda e: (
                error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline.instructions
            ),
            key="BlueVerifiedFollowers",
            param=param,
        )

    def get_list_members(
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
        return self.request(
            apiFn=self.api.get_list_members_with_http_info,
            convertFn=lambda e: error_check(e.data.list.members_timeline.timeline, e.errors).instructions,
            key="ListMembers",
            param=param,
        )

    def get_list_subscribers(
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
        return self.request(
            apiFn=self.api.get_list_subscribers_with_http_info,
            convertFn=lambda e: error_check(e.data.list.subscribers_timeline.timeline, e.errors).instructions,
            key="ListSubscribers",
            param=param,
        )

    def get_list_creation_recommended_users(
        self,
        list_id: str,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Empty unless list_id is one of the authenticated account's lists."""
        param: ParamType = {"listId": list_id}
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_list_creation_recommended_users_with_http_info,
            convertFn=lambda e: t.instructions if (t := e.data.list.recommended_users.timeline) else [],
            key="ListCreationRecommendedUsers",
            param=param,
        )

    def get_list_edit_recommended_users(
        self,
        list_id: str,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Empty unless list_id is one of the authenticated account's lists."""
        param: ParamType = {"listId": list_id}
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_list_edit_recommended_users_with_http_info,
            convertFn=lambda e: t.instructions if (t := e.data.list.recommended_users.timeline) else [],
            key="ListEditRecommendedUsers",
            param=param,
        )

    def get_list_ownerships(
        self,
        user_id: str,
        is_list_member_target_user_id: Optional[str] = None,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ListResponseType:
        """Lists owned by user_id; is_list_member_target_user_id marks the lists that user is a member of."""
        param: ParamType = {"userId": user_id}
        if is_list_member_target_user_id is not None:
            param["isListMemberTargetUserId"] = is_list_member_target_user_id
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_list_ownerships_with_http_info,
            self.flag["ListOwnerships"],
            self.ct,
            lambda e: (
                error_check(
                    error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline, e.errors
                ).instructions
            ),
            param,
            list_entries_converter,
        )

    def get_list_by_rest_id(
        self,
        list_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.TwitterList]:
        param: ParamType = {"listId": list_id}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_list_by_rest_id_with_http_info,
            self.flag["ListByRestId"],
            self.ct,
            lambda e: error_check(e.data, e.errors).list,
            param,
        )

    def get_list_search_timeline(
        self,
        raw_query: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ListResponseType:
        param: ParamType = {"rawQuery": raw_query}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_list_search_timeline_with_http_info,
            self.flag["ListSearchTimeline"],
            self.ct,
            lambda e: error_check(e.data.search_by_raw_query.list_search_timeline.timeline, e.errors).instructions,
            param,
            list_entries_converter,
        )

    def get_combined_lists(
        self,
        user_id: str,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ListResponseType:
        """Lists a user owns or follows."""
        param: ParamType = {"userId": user_id}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_combined_lists_with_http_info,
            self.flag["CombinedLists"],
            self.ct,
            lambda e: (
                error_check(
                    error_check(error_check(e.data.user, e.errors).result.timeline, e.errors).timeline, e.errors
                ).instructions
            ),
            param,
            list_entries_converter,
        )

    def get_lists_management_page_timeline(
        self,
        cursor: Optional[str] = None,
        count: Optional[int] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ListResponseType:
        """The account's lists management page."""
        param: ParamType = {}
        if cursor is not None:
            param["cursor"] = cursor
        if count is not None:
            param["count"] = count
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_lists_management_page_timeline_with_http_info,
            self.flag["ListsManagementPageTimeline"],
            self.ct,
            lambda e: error_check(e.data.viewer.list_management_timeline.timeline, e.errors).instructions,
            param,
            list_entries_converter,
        )

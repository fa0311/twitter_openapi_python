from typing import Any, Callable, Dict, List, Optional, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from x_client_transaction import ClientTransaction

from twitter_openapi_python.models import TwitterApiUtilsResponse, UserApiUtilsData
from twitter_openapi_python.utils import (
    build_response,
    data_request,
    error_check,
    get_kwargs,
    user_or_null_converter,
)

T = TypeVar("T")
ResponseType = TwitterApiUtilsResponse[UserApiUtilsData]
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class UserApiUtils:
    api: twitter.UserApi
    flag: ParamType

    def __init__(self, api: twitter.UserApi, flag: ParamType, ct: ClientTransaction):
        self.api = api
        self.flag = flag
        self.ct = ct

    def request(
        self,
        apiFn: "ApiFnType[T]",
        convertFn: Callable[[T], models.UserResults],
        key: str,
        param: ParamType,
    ) -> ResponseType:
        args = get_kwargs(flag=self.flag[key], additional=param, ct=self.ct)
        res = apiFn(**args)
        result = convertFn(res.data)
        if result.result is None:
            raise Exception("No user")
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
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        param: ParamType = {"screen_name": screen_name}
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_screen_name_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors),
            key="UserByScreenName",
            param=param,
        )

    def get_user_by_rest_id(
        self,
        user_id: str,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Deprecated: X answers 403 outside a browser since 2026-10."""
        param: ParamType = {"userId": user_id}
        if extra_param is not None:
            param.update(extra_param)
        return self.request(
            apiFn=self.api.get_user_by_rest_id_with_http_info,
            convertFn=lambda e: error_check(e.data.user, e.errors),
            key="UserByRestId",
            param=param,
        )

    def get_about_account_query(
        self,
        screen_name: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.AboutAccountUser]:
        """The "About this account" panel: join date, where the account is based, username changes, verification."""
        param: ParamType = {"screenName": screen_name}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_about_account_query_with_http_info,
            self.flag["AboutAccountQuery"],
            self.ct,
            lambda e: error_check(e.data, e.errors).user_result_by_screen_name.result,
            param,
        )

    def get_viewer_badge_counts(
        self,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.BadgeCounts]:
        """Unread counts (notifications, DMs, XChat) of the authenticated account."""
        param: ParamType = {}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_viewer_badge_counts_with_http_info,
            self.flag["ViewerBadgeCounts"],
            self.ct,
            lambda e: error_check(e.data, e.errors).viewer_v2.user_results.result.badge_counts,
            param,
        )

    def get_fetch_draft_tweets(
        self,
        ascending: Optional[bool] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[List[models.DraftTweet]]:
        param: ParamType = {}
        if ascending is not None:
            param["ascending"] = ascending
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_fetch_draft_tweets_with_http_info,
            self.flag["FetchDraftTweets"],
            self.ct,
            lambda e: error_check(e.data, e.errors).viewer.draft_list.response_data,
            param,
        )

    def get_fetch_scheduled_tweets(
        self,
        ascending: Optional[bool] = None,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[List[Dict[str, Any]]]:
        """Items are untyped: no scheduled post has been recorded yet."""
        param: ParamType = {}
        if ascending is not None:
            param["ascending"] = ascending
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_fetch_scheduled_tweets_with_http_info,
            self.flag["FetchScheduledTweets"],
            self.ct,
            lambda e: error_check(e.data, e.errors).viewer.scheduled_tweet_list,
            param,
        )

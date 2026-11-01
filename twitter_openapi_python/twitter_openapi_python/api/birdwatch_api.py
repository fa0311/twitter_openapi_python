from typing import Any, Optional

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


class BirdwatchApiUtils:
    """Community Notes."""

    api: twitter.BirdwatchApi
    flag: ParamType

    def __init__(self, api: twitter.BirdwatchApi, flag: ParamType, ct: Optional[ClientTransaction]):
        self.api = api
        self.flag = flag
        self.ct = ct

    def get_birdwatch_fetch_alias_self_select_status(
        self,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.BirdwatchAliasSelfSelectStatus]:
        param: ParamType = {}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_birdwatch_fetch_alias_self_select_status_with_http_info,
            self.flag["BirdwatchFetchAliasSelfSelectStatus"],
            self.ct,
            lambda e: error_check(e.data, e.errors).authenticated_user_birdwatch_alias_self_select_status,
            param,
        )

    def get_birdwatch_fetch_authenticated_user_profile(
        self,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.BirdwatchProfile]:
        param: ParamType = {}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_birdwatch_fetch_authenticated_user_profile_with_http_info,
            self.flag["BirdwatchFetchAuthenticatedUserProfile"],
            self.ct,
            lambda e: error_check(e.data, e.errors).authenticated_user_birdwatch_profile,
            param,
        )

    def get_birdwatch_fetch_birdwatch_profile(
        self,
        alias: str,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.BirdwatchProfile]:
        param: ParamType = {"alias": alias}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_birdwatch_fetch_birdwatch_profile_with_http_info,
            self.flag["BirdwatchFetchBirdwatchProfile"],
            self.ct,
            lambda e: error_check(e.data, e.errors).birdwatch_profile_by_alias,
            param,
        )

    def get_birdwatch_fetch_global_timeline(
        self,
        cursor: Optional[str] = None,
        extra_param: Optional[ParamType] = None,
    ) -> ResponseType:
        """Posts with notes on the Community Notes home page (first tab)."""
        param: ParamType = {}
        if cursor is not None:
            param["cursor"] = cursor
        if extra_param is not None:
            param.update(extra_param)
        return timeline_request(
            self.api.get_birdwatch_fetch_global_timeline_with_http_info,
            self.flag["BirdwatchFetchGlobalTimeline"],
            self.ct,
            lambda e: error_check(
                e.data.viewer.birdwatch_home_page.body.initial_timeline.timeline.timeline, e.errors
            ).instructions,
            param,
            tweet_entries_converter,
        )

    def get_birdwatch_fetch_public_data(
        self,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[models.BirdwatchPublicDataFileBundle]:
        """Download urls of the latest public data files."""
        param: ParamType = {}
        if extra_param is not None:
            param.update(extra_param)
        return data_request(
            self.api.get_birdwatch_fetch_public_data_with_http_info,
            self.flag["BirdwatchFetchPublicData"],
            self.ct,
            lambda e: error_check(e.data, e.errors).birdwatch_latest_public_data_file_bundle,
            param,
        )

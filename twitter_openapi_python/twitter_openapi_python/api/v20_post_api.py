from typing import Any, Callable, Optional, TypeVar

import twitter_openapi_python_generated as twitter

from twitter_openapi_python.models import TwitterApiUtilsResponse
from twitter_openapi_python.utils import build_response, get_legacy_kwargs

T = TypeVar("T")
ApiFnType = Callable[..., twitter.ApiResponse[T]]
ParamType = dict[str, Any]


class V20PostApiUtils:
    api: twitter.V20PostApi
    flag: ParamType

    def __init__(self, api: twitter.V20PostApi, flag: ParamType):
        self.api = api
        self.flag = flag

    def request(
        self,
        apiFn: "ApiFnType[T]",
        key: str,
        param: ParamType,
    ) -> TwitterApiUtilsResponse[T]:
        args = get_legacy_kwargs(flag=self.flag[key], additional=param)
        res = apiFn(**args)
        return build_response(response=res, data=res.data)

    def post_timeline_feedback(
        self,
        feedback_type: str,
        action_metadata: str,
        undo: bool = False,
        extra_param: Optional[ParamType] = None,
    ) -> TwitterApiUtilsResponse[None]:
        """feedback_type and action_metadata are the query of a feedbackUrl in the timeline."""
        param = {
            "feedback_type": feedback_type,
            "action_metadata": action_metadata,
            "feedback_type2": feedback_type,  # the form repeats the query's feedback_type
            "undo": "true" if undo else "false",
        }
        if extra_param is not None:
            param.update(extra_param)

        response = self.request(
            apiFn=self.api.post_timeline_feedback_with_http_info,
            param=param,
            key="timeline/feedback.json",
        )
        return response

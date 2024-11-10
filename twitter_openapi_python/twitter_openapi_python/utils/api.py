import json
from typing import Any, Dict, List, Mapping, Optional, TypeGuard, TypeVar

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.models import (
    ApiUtilsHeader,
    CursorApiUtilsResponse,
    TweetApiUtilsData,
    TwitterApiUtilsRaw,
    TwitterApiUtilsResponse,
    UserApiUtilsData,
)

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
ParamType = dict[str, Any]


def flat(matrix: List[List[T]]) -> List[T]:
    return [x for row in matrix for x in row]


def non_nullable(x: Optional[T]) -> T:
    if x is None:
        raise Exception("No data")
    return x


def non_nullable_list(x: List[Optional[T]]) -> List[T]:
    def filter_fn(x: Optional[T]) -> TypeGuard[T]:
        return x is not None

    return list(filter(filter_fn, x))


def get_kwargs(flag: ParamType, additional: ParamType) -> ParamType:
    assert flag is not None
    kwargs = {"path_query_id": flag["queryId"]}
    if flag.get("variables") is not None:
        kwargs["variables"] = json.dumps(flag["variables"] | additional)
    if flag.get("features") is not None:
        kwargs["features"] = json.dumps(flag["features"])
    if flag.get("fieldToggles") is not None:
        kwargs["field_toggles"] = json.dumps(flag["fieldToggles"])
    return kwargs


def get_legacy_kwargs(flag: ParamType, additional: ParamType) -> ParamType:
    assert flag is not None

    def to_snake_case(x: str) -> str:
        return "".join(["_" + i.lower() if i.isupper() else i for i in x]).lstrip("_")

    res = {to_snake_case(k): v for k, v in flag.items()}

    return res | additional


def error_check(data: Optional[T], error: Optional[List[models.ErrorResponse]]) -> T:
    if data is None:
        if error is None:
            raise Exception("No data")
        else:
            raise Exception(", ".join([x.message for x in error]))
    return data


def instruction_to_entry(
    input: List[models.InstructionUnion],
) -> List[models.TimelineAddEntry]:
    def map_fn(x: models.InstructionUnion) -> List[models.TimelineAddEntry]:
        one_of = x.actual_instance

        if isinstance(one_of, models.TimelineAddEntries):
            return one_of.entries
        elif isinstance(one_of, models.TimelineReplaceEntry):
            return [one_of.entry]
        else:
            return []

    return flat(list(map(map_fn, input)))


def tweet_entries_converter(
    input: List[models.TimelineAddEntry],
) -> List[TweetApiUtilsData]:
    def map_fn(x: models.TimelineAddEntry) -> Optional[List[TweetApiUtilsData]]:
        one_of = x.content.actual_instance

        if isinstance(one_of, models.TimelineTimelineItem):
            item = one_of.item_content.actual_instance
            if isinstance(item, models.TimelineTweet):
                return non_nullable_list(
                    [
                        build_tweet_api_utils(
                            result=item.tweet_results,
                            promoted_metadata=item.promoted_metadata,
                            reply=[],
                        )
                    ]
                )
        elif isinstance(one_of, models.TimelineTimelineModule):
            module = one_of.items or []
            timelineList = non_nullable_list(list(map(map_fn_2, module)))
            if len(timelineList) == 0:
                return None
            if one_of.display_type == models.DisplayType.VERTICALGRID:
                return non_nullable_list(
                    [
                        build_tweet_api_utils(
                            result=x.tweet_results,
                            promoted_metadata=x.promoted_metadata,
                            reply=[],
                        )
                        for x in timelineList
                    ]
                )
            else:
                timeline = timelineList[0]
                return non_nullable_list(
                    [
                        build_tweet_api_utils(
                            result=timeline.tweet_results,
                            promoted_metadata=timeline.promoted_metadata,
                            reply=timelineList[1:],
                        )
                    ]
                )

    def map_fn_2(x: models.ModuleItem) -> Optional[models.TimelineTweet]:
        item = x.item.item_content.actual_instance
        if isinstance(item, models.TimelineTweet):
            return item

    return flat(non_nullable_list(list(map(map_fn, input))))


def user_or_null_converter(user: models.UserUnion) -> Optional[models.User]:
    if isinstance(user.actual_instance, models.User):
        return user.actual_instance


def build_tweet_api_utils(
    result: models.ItemResult,
    promoted_metadata: Optional[dict[str, Any]] = None,
    reply: Optional[List[models.TimelineTweet]] = None,
) -> Optional[TweetApiUtilsData]:
    tweet = tweet_results_converter(result)
    if tweet is None:
        return None
    if tweet.core is None:
        return None
    if tweet.core.user_results.result is None:
        return None
    user = user_or_null_converter(tweet.core.user_results.result)
    if user is None:
        return None

    quoted = tweet.quoted_status_result

    retweeted = None if tweet.legacy is None else tweet.legacy.retweeted_status_result

    def reply_fn(x: models.TimelineTweet) -> Optional[TweetApiUtilsData]:
        return build_tweet_api_utils(x.tweet_results, x.promoted_metadata, [])

    return TweetApiUtilsData(
        raw=result,
        promoted_metadata=promoted_metadata,
        tweet=tweet,
        user=user,
        replies=non_nullable_list(list(map(reply_fn, reply or []))),
        retweeted=build_tweet_api_utils(retweeted, None, []) if retweeted else None,
        quoted=build_tweet_api_utils(quoted, None, []) if quoted else None,
    )


def tweet_results_converter(tweetResults: models.ItemResult) -> Optional[models.Tweet]:
    if tweetResults.result is None:
        return None
    properties = tweetResults.result.actual_instance
    if isinstance(properties, models.Tweet):
        return properties
    elif isinstance(properties, models.TweetWithVisibilityResults):
        return properties.tweet
    elif isinstance(properties, models.TweetTombstone):
        return None
    raise Exception()


def user_entries_converter(
    item: list[models.TimelineAddEntry],
) -> list[models.UserResults]:
    def map_fn(x: models.TimelineAddEntry) -> Optional[models.UserResults]:
        one_of = x.content.actual_instance
        if isinstance(one_of, models.TimelineTimelineItem):
            item = one_of.item_content.actual_instance
            if isinstance(item, models.TimelineUser):
                return item.user_results

    return non_nullable_list(list(map(map_fn, item)))


def user_result_converter(item: list[models.UserResults]) -> List[UserApiUtilsData]:
    def map_fn(raw: models.UserResults) -> Optional[UserApiUtilsData]:
        if raw.result is None:
            return None
        user = user_or_null_converter(raw.result)
        if user is None:
            return None

        return UserApiUtilsData(
            raw=raw,
            user=user,
        )

    return non_nullable_list(list(map(map_fn, item)))


def entries_cursor(item: List[models.TimelineAddEntry]) -> CursorApiUtilsResponse:
    def map_fn(x: models.TimelineAddEntry) -> Optional[models.TimelineTimelineCursor]:
        item = x.content.actual_instance
        if isinstance(item, models.TimelineTimelineCursor):
            return item
        elif isinstance(item, models.TimelineTimelineItem):
            content = item.item_content.actual_instance
            if isinstance(content, models.TimelineTimelineCursor):
                return content

    return build_cursor(non_nullable_list(list(map(map_fn, item))))


def build_cursor(list: list[models.TimelineTimelineCursor]) -> CursorApiUtilsResponse:
    def find_fn_1(x: models.TimelineTimelineCursor) -> bool:
        return x.cursor_type == models.CursorType.TOP

    def find_fn_2(x: models.TimelineTimelineCursor) -> bool:
        return x.cursor_type == models.CursorType.BOTTOM

    return CursorApiUtilsResponse(
        top=next(filter(find_fn_1, list), None),
        bottom=next(filter(find_fn_2, list), None),
    )


def build_header(headers: Dict[str, str]) -> ApiUtilsHeader:
    return ApiUtilsHeader(
        raw=headers,
        connection_hash=headers["x-connection-hash"],
        content_type_options=headers["x-content-type-options"],
        frame_options=headers["x-frame-options"],
        rate_limit_limit=int(headers.get("x-rate-limit-limit", 0)),
        rate_limit_remaining=int(headers.get("x-rate-limit-remaining", 0)),
        rate_limit_reset=int(headers.get("x-rate-limit-reset", 0)),
        response_time=int(headers["x-response-time"]),
        tfe_preserve_body=headers.get("x-tfe-preserve-body") == "true",
        transaction_id=headers["x-transaction-id"],
        twitter_response_tags=headers["x-twitter-response-tags"],
        xss_protection=int(headers["x-xss-protection"]),
    )


def build_response(response: twitter.ApiResponse, data: T1) -> TwitterApiUtilsResponse[T1]:
    if response.headers is None:
        raise Exception("headers is None")

    if isinstance(response.headers, Dict):
        header = build_header(response.headers)
    elif isinstance(response.headers, Mapping):
        header = build_header(dict(response.headers))
    else:
        raise Exception("headers is not a dict")

    return TwitterApiUtilsResponse(
        raw=TwitterApiUtilsRaw(response=response),
        header=header,
        data=data,
    )

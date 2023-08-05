import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from typing import Dict, List, Type, TypeGuard, TypeVar, Optional, Any
from twitter_openapi_python.models import (
    ApiUtilsHeader,
    PostApiUtilsHeader,
    CursorApiUtilsResponse,
    TweetApiUtilsData,
    UserApiUtilsData,
)
from twitter_openapi_python.models.response import (
    TwitterApiUtilsRaw,
    TwitterApiUtilsResponse,
)

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")


def flat(matrix: List[List[T]]) -> List[T]:
    return [x for row in matrix for x in row]


def non_nullable_list(x: List[Optional[T]]) -> List[T]:
    def filter_fn(x: Optional[T]) -> TypeGuard[T]:
        return x is not None

    return list(filter(filter_fn, x))


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
    def map_fn(x: models.TimelineAddEntry) -> Optional[TweetApiUtilsData]:
        one_of = x.content.actual_instance

        if isinstance(one_of, models.TimelineTimelineItem):
            item = one_of.item_content.actual_instance
            if isinstance(item, models.TimelineTweet):
                return buildTweetApiUtils(
                    result=item.tweet_results,
                    promoted_metadata=item.promoted_metadata,
                    reply=[],
                )
        elif isinstance(one_of, models.TimelineTimelineModule):
            module = one_of.items or []
            timelineList = non_nullable_list(list(map(map_fn_2, module)))
            if len(timelineList) == 0:
                return None
            timeline = timelineList[0]
            return buildTweetApiUtils(
                result=timeline.tweet_results,
                promoted_metadata=timeline.promoted_metadata,
                reply=timelineList[1:],
            )

    def map_fn_2(x: models.ModuleItem) -> Optional[models.TimelineTweet]:
        item = x.item.item_content.actual_instance
        if isinstance(item, models.TimelineTweet):
            return item

    return non_nullable_list(list(map(map_fn, input)))


def buildTweetApiUtils(
    result: models.ItemResult,
    promoted_metadata: Optional[dict[str, Any]],
    reply: List[models.TimelineTweet],
) -> Optional[TweetApiUtilsData]:
    tweet = tweetResultsConverter(result)
    if tweet is None:
        return None

    quoted = tweet.quoted_status_result

    # retweeted = tweet.legacy.retweeted_status_result
    def reply_fn(x: models.TimelineTweet) -> Optional[TweetApiUtilsData]:
        return buildTweetApiUtils(x.tweet_results, x.promoted_metadata, [])

    return TweetApiUtilsData(
        raw=result,
        promoted_metadata=promoted_metadata,
        tweet=tweet,
        user=tweet.core.user_results.result,
        replies=non_nullable_list(list(map(reply_fn, reply))),
        quoted=buildTweetApiUtils(quoted, None, []) if quoted else None,
    )


def tweetResultsConverter(tweetResults: models.ItemResult) -> Optional[models.Tweet]:
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
) -> list[models.TimelineUser]:
    def map_fn(x: models.TimelineAddEntry) -> Optional[models.TimelineUser]:
        one_of = x.content.actual_instance
        if isinstance(one_of, models.TimelineTimelineItem):
            item = one_of.item_content.actual_instance
            if isinstance(item, models.TimelineUser):
                return item

    return non_nullable_list(list(map(map_fn, item)))


def build_user_response(user: models.TimelineUser) -> UserApiUtilsData:
    return UserApiUtilsData(
        raw=user,
        user=user.user_results.result,
    )


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
        rate_limit_limit=int(headers["x-rate-limit-limit"]),
        rate_limit_remaining=int(headers["x-rate-limit-remaining"]),
        rate_limit_reset=int(headers["x-rate-limit-reset"]),
        response_time=int(headers["x-response-time"]),
        tfe_preserve_body=headers["x-tfe-preserve-body"] == "true",
        transaction_id=headers["x-transaction-id"],
        twitter_response_tags=headers["x-twitter-response-tags"],
        xss_protection=int(headers["x-xss-protection"]),
    )


def post_build_header(headers: Dict[str, str]) -> PostApiUtilsHeader:
    return PostApiUtilsHeader(
        raw=headers,
        connection_hash=headers["x-connection-hash"],
        content_type_options=headers["x-content-type-options"],
        frame_options=headers["x-frame-options"],
        response_time=int(headers["x-response-time"]),
        tfe_preserve_body=headers["x-tfe-preserve-body"] == "true",
        transaction_id=headers["x-transaction-id"],
        xss_protection=int(headers["x-xss-protection"]),
    )


def build_response(
    response: twitter.ApiResponse,
    data: T1,
    type: Type[T2],
) -> TwitterApiUtilsResponse[T1, T2]:
    if response.headers is None:
        raise Exception("headers is None")

    if type == ApiUtilsHeader:
        header = build_header(response.headers)
    elif type == PostApiUtilsHeader:
        header = post_build_header(response.headers)
    else:
        raise Exception("type must be ApiUtilsHeader or PostApiUtilsHeader")

    return TwitterApiUtilsResponse(
        raw=TwitterApiUtilsRaw(response=response),
        header=header,
        data=data,
    )  # type: ignore

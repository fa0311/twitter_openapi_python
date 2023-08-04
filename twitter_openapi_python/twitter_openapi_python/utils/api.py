import twitter_openapi_python_generated.models as models
from typing import List, TypeGuard, TypeVar, Optional, Any

from urllib3 import HTTPHeaderDict

from twitter_openapi_python.models import (
    ApiUtilsHeader,
    PostApiUtilsHeader,
    CursorApiUtilsResponse,
    TweetApiUtilsData,
    UserApiUtilsData,
)

T = TypeVar("T")


def flat(matrix: List[List[T]]) -> List[T]:
    return [x for row in matrix for x in row]


def nonNullableList(x: List[Optional[T]]) -> List[T]:
    def filter_fn(x: Optional[T]) -> TypeGuard[T]:
        return x is not None

    return list(filter(filter_fn, x))


def instructionToEntry(
    input: List[models.InstructionUnion],
) -> List[models.TimelineAddEntry]:
    def map_fn(x: models.InstructionUnion) -> List[models.TimelineAddEntry]:
        if x.actual_instance.type == models.InstructionType.TIMELINEADDENTRIES:
            res = x.actual_instance.entries
            return res
        elif x.actual_instance.type == models.InstructionType.TIMELINEREPLACEENTRY:
            res = [x.actual_instance.entry]
            return res
        else:
            return []

    return flat(list(map(map_fn, input)))


def tweetEntriesConverter(
    input: List[models.TimelineAddEntry],
) -> List[TweetApiUtilsData]:
    def map_fn(x: models.TimelineAddEntry) -> Optional[TweetApiUtilsData]:
        one_of = x.content.actual_instance
        if one_of.entry_type == models.ContentEntryType.TIMELINETIMELINEITEM:
            item = one_of.item_content
            if item.actual_instance.typename == models.TypeName.TIMELINETWEET:
                timeline = item.actual_instance
                return buildTweetApiUtils(
                    result=timeline.tweet_results,
                    promoted_metadata=timeline.promoted_metadata,
                    reply=[],
                )
            else:
                return None
        elif one_of.entry_type == models.ContentEntryType.TIMELINETIMELINEMODULE:
            module = one_of.items or []
            timelineList = nonNullableList(list(map(map_fn_2, module)))
            if len(timelineList) == 0:
                return None
            timeline = timelineList[0]
            return buildTweetApiUtils(
                result=timeline.tweet_results,
                promoted_metadata=timeline.promoted_metadata,
                reply=timelineList[1:],
            )
        else:
            return None

    def map_fn_2(x: models.ModuleItem) -> Optional[models.TimelineTweet]:
        item = x.item.item_content.actual_instance
        if item.typename == models.TypeName.TIMELINETWEET:
            return item
        return None

    return nonNullableList(list(map(map_fn, input)))


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
        reply=nonNullableList(list(map(reply_fn, reply))),
        quoted=buildTweetApiUtils(quoted, None, []) if quoted else None,
    )


def tweetResultsConverter(tweetResults: models.ItemResult) -> Optional[models.Tweet]:
    properties = tweetResults.result.actual_instance
    if properties.typename == models.TypeName.TWEET:
        return properties
    elif properties.typename == models.TypeName.TWEETWITHVISIBILITYRESULTS:
        return properties.tweet
    elif properties.typename == models.TypeName.TWEETTOMBSTONE:
        return None
    raise Exception()


def userEntriesConverter(
    item: list[models.TimelineAddEntry],
) -> list[models.TimelineUser]:
    def map_fn(x: models.TimelineAddEntry) -> Optional[models.TimelineUser]:
        one_of = x.content.actual_instance
        if one_of.typename == models.TypeName.TIMELINETIMELINEITEM:
            item = one_of.item_content
            if item.actual_instance.typename == models.TypeName.TIMELINEUSER:
                return item.actual_instance

    return nonNullableList(list(map(map_fn, item)))


def buildUserResponse(user: models.TimelineUser) -> UserApiUtilsData:
    return UserApiUtilsData(
        raw=user,
        user=user.user_results.result,
    )


def entriesCursor(item: models.TimelineAddEntry) -> CursorApiUtilsResponse:
    def map_fn(x: models.TimelineAddEntry) -> Optional[models.TimelineTimelineCursor]:
        item = x.content.actual_instance
        if item.entry_type == models.ContentEntryType.TIMELINETIMELINECURSOR:
            return item
        elif item.entry_type == models.ContentEntryType.TIMELINETIMELINEITEM:
            content = item.item_content.actual_instance
            if content.item_type == models.ContentItemType.TIMELINETIMELINECURSOR:
                return content

    return buildCursor(nonNullableList(list(map(map_fn, item))))


def buildCursor(list: list[models.TimelineTimelineCursor]) -> CursorApiUtilsResponse:
    def find_fn_1(x: models.TimelineTimelineCursor) -> bool:
        return x.cursor_type == models.CursorType.TOP

    def find_fn_2(x: models.TimelineTimelineCursor) -> bool:
        return x.cursor_type == models.CursorType.BOTTOM

    return CursorApiUtilsResponse(
        top=next(filter(find_fn_1, list), None),
        bottom=next(filter(find_fn_2, list), None),
    )


def buildHeader(headers: HTTPHeaderDict) -> ApiUtilsHeader:
    return ApiUtilsHeader(
        raw=headers,
        connection_hash=headers.get("x-connection-hash"),
        content_type_options=headers.get("x-content-type-options"),
        frame_options=headers.get("x-frame-options"),
        rate_limit_limit=int(headers.get("x-rate-limit-limit")),
        rate_limit_remaining=int(headers.get("x-rate-limit-remaining")),
        rate_limit_reset=int(headers.get("x-rate-limit-reset")),
        response_time=int(headers.get("x-response-time")),
        tfe_preserve_body=headers.get("x-tfe-preserve-body") == "true",
        transaction_id=headers.get("x-transaction-id"),
        twitter_response_tags=headers.get("x-twitter-response-tags"),
        xss_protection=int(headers.get("x-xss-protection")),
    )


def postBuildHeader(headers: HTTPHeaderDict) -> PostApiUtilsHeader:
    return PostApiUtilsHeader(
        raw=headers,
        connection_hash=headers.get("x-connection-hash"),
        content_type_options=headers.get("x-content-type-options"),
        frame_options=headers.get("x-frame-options"),
        response_time=int(headers.get("x-response-time")),
        tfe_preserve_body=headers.get("x-tfe-preserve-body") == "true",
        transaction_id=headers.get("x-transaction-id"),
        xss_protection=int(headers.get("x-xss-protection")),
    )

import twitter_openapi_python_generated.models as models
from typing import List, TypeGuard, TypeVar, Optional, Any, Union

from twitter_openapi_python.model.tweet import TweetApiUtilsData

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
        actual_instance = x.content.actual_instance
        if actual_instance.entry_type == models.ContentEntryType.TIMELINETIMELINEITEM:
            item = actual_instance.item_content
            if item.actual_instance.item_type == "TimelineTweet":
                timeline = item.actual_instance
                return buildTweetApiUtils(
                    result=timeline.tweet_results,
                    promoted_metadata=timeline.promoted_metadata,
                    reply=[],
                )
            else:
                return None
        elif actual_instance.entry_type == "TimelineTimelineModule":
            item = actual_instance.items or []
            timelineList = nonNullableList(list(map(map_fn_2, item)))
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
        if x.item.item_content.actual_instance.item_type == "TimelineTweet":
            return x.item.item_content.actual_instance
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
    properties: Any = tweetResults.result.actual_instance
    if properties.typename == models.TypeName.TWEET:
        return properties
    elif properties.typename == models.TypeName.TWEETWITHVISIBILITYRESULTS:
        return properties.tweet
    elif properties.typename == models.TypeName.TWEETTOMBSTONE:
        return None
    raise Exception()

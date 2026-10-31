import time
from collections.abc import Callable, Iterator
from typing import TypeVar

from twitter_openapi_python.models import TimelineApiUtilsResponse, TwitterApiUtilsResponse

T = TypeVar("T")
PaginateFn = Callable[[str | None], TwitterApiUtilsResponse[TimelineApiUtilsResponse[T]]]


def paginate(fetch: "PaginateFn[T]", limit: int | None = None, wait: bool = True) -> Iterator[T]:
    """Walks a timeline page by page through its bottom cursor and yields the items.

    Stops when a page brings no item, has no bottom cursor or repeats the cursor, or after `limit` items.
    Waits for the rate-limit window to reset when it is used up, unless `wait` is False.
    """
    cursor: str | None = None
    count = 0
    while True:
        response = fetch(cursor)
        for item in response.data.data:
            if limit is not None and count >= limit:
                return
            yield item
            count += 1
        bottom = response.data.cursor.bottom
        if not response.data.data or bottom is None or bottom.value == cursor:
            return
        if limit is not None and count >= limit:
            return
        cursor = bottom.value
        if wait and response.header.rate_limit_remaining == 0:
            time.sleep(max(0, response.header.rate_limit_reset - time.time()) + 1)

from typing import Any, List, Optional
from pydantic import Field
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.model.base import BaseModel
from twitter_openapi_python.model.header import ApiUtilsHeader
from twitter_openapi_python.model.timeline import ApiUtilsRaw, CursorApiUtilsResponse


class TweetApiUtilsData(BaseModel):
    raw: models.ItemResult = Field()
    tweet: models.Tweet = Field()
    user: models.User = Field()
    reply: List["TweetApiUtilsData"] = Field(default_factory=list)
    quoted: Optional["TweetApiUtilsData"] = Field(default=None)
    retweeted: Optional["TweetApiUtilsData"] = Field(default=None)
    promoted_metadata: Optional[dict[str, Any]] = Field(default=None)


class TweetListApiUtilsResponse(BaseModel):
    raw: ApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    cursor: CursorApiUtilsResponse = Field()
    data: List[TweetApiUtilsData] = Field(default_factory=list)

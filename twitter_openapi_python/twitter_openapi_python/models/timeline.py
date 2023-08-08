from typing import Any, Generic, List, Optional, TypeVar

# from twitter_openapi_python_generated.api_response import ApiResponse
import twitter_openapi_python_generated.models as models
from pydantic import Field

from twitter_openapi_python.models import BaseModel, GenericModel

T = TypeVar("T")


class ApiUtilsRaw(BaseModel):
    instruction: List[models.InstructionUnion] = Field(default_factory=list)
    entry: List[models.TimelineAddEntry] = Field(default_factory=list)


class CursorApiUtilsResponse(BaseModel):
    bottom: Optional[models.TimelineTimelineCursor] = Field(default=None)
    top: Optional[models.TimelineTimelineCursor] = Field(default=None)


class TweetApiUtilsData(BaseModel):
    raw: models.ItemResult = Field()
    tweet: models.Tweet = Field()
    user: models.User = Field()
    replies: List["TweetApiUtilsData"] = Field(default_factory=list)
    quoted: Optional["TweetApiUtilsData"] = Field(default=None)
    retweeted: Optional["TweetApiUtilsData"] = Field(default=None)
    promoted_metadata: Optional[dict[str, Any]] = Field(default=None)


class UserApiUtilsData(BaseModel):
    raw: models.UserResults = Field()
    user: models.User = Field()


class TimelineApiUtilsResponse(GenericModel, Generic[T]):
    raw: ApiUtilsRaw = Field()
    cursor: CursorApiUtilsResponse = Field()
    data: List[T] = Field(default_factory=list)

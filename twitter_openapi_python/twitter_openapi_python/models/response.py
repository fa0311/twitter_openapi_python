from pydantic import Field

from twitter_openapi_python.models.header import ApiUtilsHeader, PostApiUtilsHeader
from typing import Generic, TypeVar
import twitter_openapi_python_generated as twitter
from twitter_openapi_python.models import BaseModel, GenericModel


T = TypeVar("T")


class TwitterApiUtilsRaw(BaseModel):
    response: twitter.ApiResponse = Field()


class TwitterApiUtilsResponse(GenericModel, Generic[T]):
    raw: TwitterApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    data: T = Field()


class TwitterPostApiUtilsResponse(GenericModel, Generic[T]):
    raw: TwitterApiUtilsRaw = Field()
    header: PostApiUtilsHeader = Field()
    data: T = Field()

from pydantic import Field

from pydantic.generics import GenericModel
from twitter_openapi_python.models.header import ApiUtilsHeader, PostApiUtilsHeader
from typing import Generic, TypeVar
from twitter_openapi_python_generated.api_response import ApiResponse
from twitter_openapi_python.models.base import BaseModel


T = TypeVar("T")


class TwitterApiUtilsRaw(BaseModel):
    response: ApiResponse = Field()


class TwitterApiUtilsResponse(GenericModel, Generic[T]):
    raw: TwitterApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    data: T = Field()


class TwitterPostApiUtilsResponse(GenericModel, Generic[T]):
    raw: TwitterApiUtilsRaw = Field()
    header: PostApiUtilsHeader = Field()
    data: T = Field()

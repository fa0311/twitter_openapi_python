from typing import Generic, TypeVar

import twitter_openapi_python_generated as twitter
from pydantic import Field

from twitter_openapi_python.models import ApiUtilsHeader, BaseModel, GenericModel

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class TwitterApiUtilsRaw(BaseModel):
    response: twitter.ApiResponse = Field()


class TwitterApiUtilsResponse(GenericModel, Generic[T1]):
    raw: TwitterApiUtilsRaw = Field()
    data: T1 = Field()
    header: ApiUtilsHeader = Field()

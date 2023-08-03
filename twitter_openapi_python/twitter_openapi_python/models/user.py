from pydantic import Field
import twitter_openapi_python_generated.models as models
from twitter_openapi_python_generated.api_response import ApiResponse

from twitter_openapi_python.models.base import BaseModel
from twitter_openapi_python.models.timeline import ApiUtilsRaw

from twitter_openapi_python.models.header import ApiUtilsHeader


class UserApiUtilsResponse(BaseModel):
    raw: ApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    data: models.User = Field()


class UsersApiUtilsResponse(BaseModel):
    raw: ApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    data: models.User = Field()


class UserApiUtilsRaw(BaseModel):
    response: ApiResponse = Field()

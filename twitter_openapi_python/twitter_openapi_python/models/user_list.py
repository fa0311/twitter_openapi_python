from pydantic import Field
import twitter_openapi_python_generated.models as models

from twitter_openapi_python.models.base import BaseModel
from twitter_openapi_python.models.timeline import ApiUtilsRaw

from twitter_openapi_python.models.header import ApiUtilsHeader


class UserListApiUtilsResponse(BaseModel):
    raw: ApiUtilsRaw = Field()
    header: ApiUtilsHeader = Field()
    cursor: models.TimelineTimelineCursor = Field()
    data: models.User = Field()


class UserApiUtilsData(BaseModel):
    raw: models.TimelineUser = Field()
    user: models.User = Field()

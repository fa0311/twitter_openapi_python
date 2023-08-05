from typing import List, Optional
from pydantic import Field
import twitter_openapi_python_generated.models as models

# from twitter_openapi_python_generated.api_response import ApiResponse
from twitter_openapi_python.models.base import BaseModel


class ApiUtilsRaw(BaseModel):
    # response: ApiResponse = Field()
    instruction: List[models.InstructionUnion] = Field(default_factory=list)
    entry: List[models.TimelineAddEntry] = Field(default_factory=list)


class CursorApiUtilsResponse(BaseModel):
    bottom: Optional[models.TimelineTimelineCursor] = Field(default=None)
    top: Optional[models.TimelineTimelineCursor] = Field(default=None)

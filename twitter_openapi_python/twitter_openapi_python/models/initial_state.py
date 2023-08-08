from typing import Any, Dict, Optional

import twitter_openapi_python_generated as twitter
from pydantic import Field

from twitter_openapi_python.models import BaseModel


class InitialStateApiUtilsRaw(BaseModel):
    initial_state: Dict[str, Any] = Field()
    meta_data: Dict[str, Any] = Field()


class InitialStateApiUtilsResponse(BaseModel):
    raw: InitialStateApiUtilsRaw = Field()
    user: Optional[twitter.UserLegacy] = Field(default=None)
    session: Optional[twitter.Session] = Field(default=None)

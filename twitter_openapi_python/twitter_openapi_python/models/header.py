from typing import Dict, Optional

from pydantic import Field

from twitter_openapi_python.models import BaseModel


class ApiUtilsHeader(BaseModel):
    raw: Dict[str, str] = Field()
    connection_hash: Optional[str] = Field()
    content_type_options: Optional[str] = Field()
    frame_options: Optional[str] = Field()
    response_time: int = Field()
    tfe_preserve_body: bool = Field()
    transaction_id: Optional[str] = Field()
    xss_protection: Optional[int] = Field()
    rate_limit_limit: int = Field()
    rate_limit_remaining: int = Field()
    rate_limit_reset: int = Field()
    twitter_response_tags: Optional[str] = Field()

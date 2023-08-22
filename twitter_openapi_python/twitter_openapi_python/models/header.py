from typing import Dict

from pydantic import Field

from twitter_openapi_python.models import BaseModel


class ApiUtilsHeader(BaseModel):
    raw: Dict[str, str] = Field()
    connection_hash: str = Field()
    content_type_options: str = Field()
    frame_options: str = Field()
    response_time: int = Field()
    tfe_preserve_body: bool = Field()
    transaction_id: str = Field()
    xss_protection: int = Field()
    rate_limit_limit: int = Field()
    rate_limit_remaining: int = Field()
    rate_limit_reset: int = Field()
    twitter_response_tags: str = Field()

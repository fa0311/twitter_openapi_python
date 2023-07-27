from typing import Any

from pydantic import Field

from twitter_openapi_python.model.base import BaseModel


class ApiUtilsHeader(BaseModel):
    raw: Any = Field()
    connectionHash: str = Field()
    contentTypeOptions: str = Field()
    frameOptions: str = Field()
    rateLimitLimit: int = Field()
    rateLimitRemaining: int = Field()
    rateLimitReset: int = Field()
    responseTime: int = Field()
    tfePreserveBody: bool = Field()
    transactionId: str = Field()
    twitterResponseTags: str = Field()
    xssProtection: int = Field()

#   Headers get raw;
#   String get connectionHash;
#   String get contentTypeOptions;
#   String get frameOptions;
#   int get rateLimitLimit;
#   int get rateLimitRemaining;
#   int get rateLimitReset;
#   int get responseTime;
#   bool get tfePreserveBody;
#   String get transactionId;
#   String get twitterResponseTags;
#   int get xssProtection;

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ApiUtilsHeader:
    raw: Any = field(init=False)
    connectionHash: str = field(init=False)
    contentTypeOptions: str = field(init=False)
    frameOptions: str = field(init=False)
    rateLimitLimit: int = field(init=False)
    rateLimitRemaining: int = field(init=False)
    rateLimitReset: int = field(init=False)
    responseTime: int = field(init=False)
    tfePreserveBody: bool = field(init=False)
    transactionId: str = field(init=False)
    twitterResponseTags: str = field(init=False)
    xssProtection: int = field(init=False)

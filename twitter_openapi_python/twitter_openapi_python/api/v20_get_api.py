import twitter_openapi_python_generated as twitter
from typing import Any


class V20GetApiUtils:
    api: twitter.V20GetApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.V20GetApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

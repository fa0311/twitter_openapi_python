import twitter_openapi_python_generated as twitter
from typing import Any


class V11PostUtils:
    api: twitter.V11PostApi
    flag: dict[str, Any]

    def __init__(self, api: twitter.V11PostApi, flag: dict[str, Any]):
        self.api = api
        self.flag = flag

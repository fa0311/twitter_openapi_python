import json
import re
from typing import Any, Optional

import twitter_openapi_python_generated as twitter
import twitter_openapi_python_generated.models as models
from urllib3 import HTTPResponse

from twitter_openapi_python.models import (
    InitialStateApiUtilsRaw,
    InitialStateApiUtilsResponse,
)


class InitialStateApiUtils:
    api: twitter.ApiClient
    header: dict[str, Any]

    def __init__(self, api: twitter.ApiClient):
        self.api = api
        self.header = {
            "user-agent": self.api.user_agent,
            "cookie": self.api.cookie,
        }

    def request(self, url: str) -> HTTPResponse:
        return self.api.rest_client.request(
            "GET",
            url=url,
            headers=self.header,
        )

    def get_initial_state(self, url: str) -> InitialStateApiUtilsResponse:
        response = self.request(url=url).data.decode("utf-8")
        reg = '<script type="text/javascript" charset="utf-8" nonce="{nonce}">{any}</script>'
        js = re.search(
            reg.format(nonce=r"([a-zA-Z0-9]{48})", any=r"([\s\S]*?)"), response
        )

        if js is None:
            raise Exception("js is None")

        reg2 = "^window\\.__INITIAL_STATE__={any};window\\.__META_DATA__={any};$"

        source = re.search(reg2.format(any=r"([\s\S]*?)"), js.group(2))

        # none cast
        if source is None:
            raise Exception("source is None")

        raw = InitialStateApiUtilsRaw(
            initial_state=json.loads(source.group(1)),
            meta_data=json.loads(source.group(2)),
        )

        def get_user(e: dict[str, Any]) -> Optional[models.UserLegacy]:
            try:
                entities = e["entities"]["users"]["entities"]
                return models.UserLegacy.parse_obj(list(entities.values())[0])
            except Exception:
                # todo: fix
                return None

        def get_session(e: dict[str, Any]) -> Optional[models.Session]:
            try:
                return models.Session.parse_obj(e["session"])
            except Exception:
                return None

        return InitialStateApiUtilsResponse(
            raw=raw,
            user=get_user(raw.initial_state),
            session=get_session(raw.initial_state),
        )

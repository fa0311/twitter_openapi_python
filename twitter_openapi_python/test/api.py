import json
from pathlib import Path
import twitter_openapi_python as api


def get_client() -> api.TwitterOpenapiPythonClient:
    if Path("cookie.json").exists():
        with open("cookie.json", "r") as f:
            cookies_dict = json.load(f)
    else:
        raise Exception("cookie.json not found")

    client = api.TwitterOpenapiPython().get_client_from_cookies(
        ct0=cookies_dict["ct0"],
        authToken=cookies_dict["auth_token"],
    )

    return client

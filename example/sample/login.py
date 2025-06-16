import json
from pathlib import Path

from requests.cookies import RequestsCookieJar
from tweepy_authlib import CookieSessionUserHandler


def login():
    if Path("cookie.json").exists():
        with open("cookie.json", "r") as f:
            cookies_dict = json.load(f)

        if isinstance(cookies_dict, list):
            cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_dict}
        cookies = RequestsCookieJar()
        for key, value in cookies_dict.items():
            cookies.set(key, value)
        return CookieSessionUserHandler(cookies=cookies)
    else:
        auth_handler = CookieSessionUserHandler(
            screen_name=input("screen_name: "),
            password=input("password: "),
        )
        cookies = auth_handler.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies.get_dict(), f, ensure_ascii=False, indent=4)
        return auth_handler

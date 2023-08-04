from typing import Any


class InitialStateApi:
    flag: dict[str, Any]

    def __init__(self, flag: dict[str, Any]):
        self.flag = flag

    # todo

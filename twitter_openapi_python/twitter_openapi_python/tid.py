import random

import requests
from x_client_transaction import ClientTransaction
from x_client_transaction.constants import ADDITIONAL_RANDOM_NUMBER, DEFAULT_KEYWORD

PAIR_URL = "https://raw.githubusercontent.com/fa0311/x-client-transaction-id-pair-dict/refs/heads/main/pair.json"


class PairClientTransaction(ClientTransaction):
    """ClientTransaction built from a precomputed (verification, animationKey) pair.

    The logged-out x.com shell no longer references ondemand.s, so the key material is
    taken from https://github.com/fa0311/x-client-transaction-id-pair-dict instead.
    """

    def __init__(self, verification: str, animation_key: str):
        self.random_keyword = DEFAULT_KEYWORD
        self.random_number = ADDITIONAL_RANDOM_NUMBER
        self.key = verification
        self.key_bytes = self.get_key_bytes(key=verification)
        self.animation_key = animation_key


def get_tid(pair_url: str = PAIR_URL) -> ClientTransaction:
    pair = random.choice(requests.get(pair_url).json())
    return PairClientTransaction(verification=pair["verification"], animation_key=pair["animationKey"])

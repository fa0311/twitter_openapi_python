import logging
import unittest

import twitter_openapi_python as api
from test.api import get_client, print_tweet


class TestBirdwatchApi(unittest.TestCase):
    client: api.BirdwatchApiUtils

    def setUp(self):
        self.client = get_client().get_birdwatch_api()

    def test_get_birdwatch_fetch_alias_self_select_status(self):
        result = self.client.get_birdwatch_fetch_alias_self_select_status()
        logging.info(f"can_select: {result.data.can_select} has_selected: {result.data.has_selected}")

    def test_get_birdwatch_fetch_authenticated_user_profile(self):
        result = self.client.get_birdwatch_fetch_authenticated_user_profile()
        logging.info(result.data.alias)

    def test_get_birdwatch_fetch_birdwatch_profile(self):
        result = self.client.get_birdwatch_fetch_birdwatch_profile(alias="me")
        logging.info(result.data.alias)

    def test_get_birdwatch_fetch_global_timeline(self):
        result = self.client.get_birdwatch_fetch_global_timeline()
        for tweet in result.data.data:
            print_tweet(tweet)

    def test_get_birdwatch_fetch_public_data(self):
        result = self.client.get_birdwatch_fetch_public_data()
        logging.info(f"notes files: {len(result.data.notes.urls)}")


if __name__ == "__main__":
    unittest.main()

import logging
import unittest

import twitter_openapi_python as api
from test.api import get_client


class TestDefaultApi(unittest.TestCase):
    client: api.DefaultApiUtils

    def setUp(self):
        self.client = get_client().get_default_api()

    def test_get_profile_spotlights_query(self):
        result = self.client.get_profile_spotlights_query(screen_name="elonmusk")
        user = result.data.result

        logging.info(user.core.screen_name)
        logging.info(
            f"followed_by: {user.relationship_perspectives.followed_by} following: {user.relationship_perspectives.following}"
        )

    def test_get_tweet_result_by_rest_id(self):
        result = self.client.get_tweet_result_by_rest_id(tweet_id="1349129669258448897")

        assert result.data is not None
        assert result.data.tweet.legacy is not None
        logging.info(result.data.tweet.legacy.full_text)


if __name__ == "__main__":
    unittest.main()

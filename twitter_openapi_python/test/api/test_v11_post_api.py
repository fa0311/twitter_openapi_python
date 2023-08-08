import logging
import unittest
from test.api import get_client

import twitter_openapi_python as api


class TestV11PostApi(unittest.TestCase):
    client: api.V11PostApiUtils

    def setUp(self):
        self.client = get_client().get_v11_post_api()

    def test_post_create_friendships(self):
        result = self.client.post_create_friendships(user_id="44196397")
        logging.info(result)

    def test_post_destroy_friendships(self):
        result = self.client.post_destroy_friendships(user_id="44196397")
        logging.info(result)


if __name__ == "__main__":
    unittest.main()

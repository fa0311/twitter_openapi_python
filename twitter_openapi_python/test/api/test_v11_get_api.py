import logging
import unittest
from test.api import get_client

import twitter_openapi_python as api


class TestV11GetApi(unittest.TestCase):
    client: api.V11GetApiUtils

    def setUp(self):
        self.client = get_client().get_v11_get_api()

    def test_get_friends_following_list(self):
        result = self.client.get_friends_following_list(user_id="44196397")
        logging.info(result)

    def test_get_search_typeahead(self):
        result = self.client.get_search_typeahead(q="test")
        logging.info(result)


if __name__ == "__main__":
    unittest.main()

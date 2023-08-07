import logging
import unittest
import twitter_openapi_python as api
from test.api import get_client


class TestV20GetApi(unittest.TestCase):
    client: api.V20GetApiUtils

    def setUp(self):
        self.client = get_client().get_v20_get_api()

    def test_get_search_adaptive(self):
        result = self.client.get_search_adaptive(q="test")
        logging.info(result)


if __name__ == "__main__":
    unittest.main()

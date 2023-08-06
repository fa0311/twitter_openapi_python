import unittest
import twitter_openapi_python as api
from test.api import get_client, print_user


class TestUserApi(unittest.TestCase):
    client: api.UserApiUtils

    def setUp(self):
        self.client = get_client().get_user_api()

    def test_get_user_by_screen_name(self):
        result = self.client.get_user_by_screen_name(screen_name="elonmusk")
        print_user(result.data)

    def test_get_user_by_rest_id(self):
        result = self.client.get_user_by_rest_id(user_id="44196397")
        print_user(result.data)


if __name__ == "__main__":
    unittest.main()

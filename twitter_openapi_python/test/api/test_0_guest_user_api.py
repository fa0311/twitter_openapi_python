import unittest

import twitter_openapi_python as api
from test.api import get_guest_client, print_user


class TestGuestUserApi(unittest.TestCase):
    client: api.UserApiUtils

    def setUp(self):
        self.client = get_guest_client().get_user_api()

    def test_get_user_by_screen_name(self):
        result = self.client.get_user_by_screen_name(screen_name="elonmusk")
        print_user(result.data)


if __name__ == "__main__":
    unittest.main()

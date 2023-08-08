import unittest
from test.api import get_client, print_legacy_user

import twitter_openapi_python as api


class TestUserApi(unittest.TestCase):
    client: api.UsersApiUtils

    def setUp(self):
        self.client = get_client().get_users_api()

    def test_get_users_by_rest_ids(self):
        result = self.client.get_users_by_rest_ids(user_ids=["44196397", "44196397"])
        for user in result.data:
            print_legacy_user(user.user.legacy)


if __name__ == "__main__":
    unittest.main()

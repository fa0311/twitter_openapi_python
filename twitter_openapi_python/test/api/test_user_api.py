import unittest
import logging
import twitter_openapi_python as api
from test.api import get_client


class TestUserApi(unittest.TestCase):
    client: api.UserApiUtils

    def setUp(self):
        self.client = get_client().get_user_api()

    def test_get_user_by_screen_name(self):
        result = self.client.get_user_by_screen_name(screen_name="elonmusk")
        legacy = result.data.legacy
        logging.info(legacy.screen_name)
        logging.info(f"followed_by: {legacy.followed_by} following: {legacy.following}")

    def test_get_user_by_rest_id(self):
        result = self.client.get_user_by_rest_id(user_id="44196397")
        legacy = result.data.legacy
        logging.info(legacy.screen_name)
        logging.info(f"followed_by: {legacy.followed_by} following: {legacy.following}")

    # def test_get_users_by_rest_ids(self):
    #     result = self.client.get_users_by_rest_ids(user_ids=["44196397", "44196397"])
    #     for user in result.data:
    #         legacy = user.legacy
    #         logging.info(legacy.screen_name)
    #         logging.info(
    #             f"followed_by: {legacy.followed_by} following: {legacy.following}"
    #         )


if __name__ == "__main__":
    unittest.main()

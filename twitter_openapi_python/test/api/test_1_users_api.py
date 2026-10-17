import logging
import unittest
from test.api import get_client, print_legacy_user

import twitter_openapi_python as api
import twitter_openapi_python_generated.models as models


class TestUserApi(unittest.TestCase):
    client: api.UsersApiUtils

    def setUp(self):
        self.client = get_client().get_users_api()

    @unittest.skip(
        "X answers UserByRestId / UsersByRestIds with 403 outside a browser (Cloudflare), the parameters are the frontend's"
    )
    def test_get_users_by_rest_ids(self):
        result = self.client.get_users_by_rest_ids(user_ids=["44196397", "44196397"])
        for user in result.data:
            print_legacy_user(user.user.legacy)

    def test_get_users_verified_avatars(self):
        result = self.client.get_users_verified_avatars(user_ids=["44196397"])
        for user in result.data:
            logging.info(f"{user.rest_id}: blue={user.is_blue_verified} shape={user.profile_image_shape}")

    def test_get_sidebar_user_recommendations(self):
        result = self.client.get_sidebar_user_recommendations(profile_user_id="44196397")
        for rec in result.data:
            user = rec.user_results.result.actual_instance
            logging.info(user.core.screen_name if isinstance(user, models.User) and user.core else type(user).__name__)


if __name__ == "__main__":
    unittest.main()

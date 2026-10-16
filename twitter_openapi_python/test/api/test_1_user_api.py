import logging
import unittest
from test.api import get_client, print_user

import twitter_openapi_python as api


class TestUserApi(unittest.TestCase):
    client: api.UserApiUtils

    def setUp(self):
        self.client = get_client().get_user_api()

    def test_get_user_by_screen_name(self):
        result = self.client.get_user_by_screen_name(screen_name="elonmusk")
        print_user(result.data)

    @unittest.skip("X answers UserByRestId / UsersByRestIds with 403 outside a browser (Cloudflare), the parameters are the frontend's")
    def test_get_user_by_rest_id(self):
        result = self.client.get_user_by_rest_id(user_id="44196397")
        print_user(result.data)

    def test_get_viewer_badge_counts(self):
        result = self.client.get_viewer_badge_counts()
        logging.info(f"unread: {result.data.total_unread_count}")

    def test_get_fetch_draft_tweets(self):
        result = self.client.get_fetch_draft_tweets()
        for draft in result.data:
            logging.info(draft.tweet_create_request.status)

    def test_get_fetch_scheduled_tweets(self):
        result = self.client.get_fetch_scheduled_tweets()
        logging.info(f"scheduled: {len(result.data)}")


if __name__ == "__main__":
    unittest.main()

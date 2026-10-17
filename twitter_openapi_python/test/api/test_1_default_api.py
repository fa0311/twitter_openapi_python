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

    def test_get_authenticate_periscope(self):
        result = self.client.get_authenticate_periscope()
        logging.info(f"token length: {len(result.data)}")

    def test_get_creator_studio_tab_bar_item_query(self):
        result = self.client.get_creator_studio_tab_bar_item_query()
        logging.info(f"tasks: {len(result.data.xpayments_audience_rewards_tasks)}")

    def test_get_data_saver_mode(self):
        result = self.client.get_data_saver_mode()
        logging.info(result.data.viewer)

    def test_get_grok_home(self):
        result = self.client.get_grok_home()
        logging.info(f"grok {result.data.grok_version}: {[m.name for m in result.data.grok_model_options]}")

    def test_get_pinned_timelines(self):
        result = self.client.get_pinned_timelines()
        logging.info(f"pinned: {len(result.data.pinned_timelines)}")

    def test_get_broadcast_query(self):
        result = self.client.get_broadcast_query(id="1BRKjmPYymWxw")
        logging.info(f"{result.data.status} ({result.data.state}, {result.data.total_watched} watched)")

    def test_get_audio_space_by_id(self):
        result = self.client.get_audio_space_by_id(id="1qxoNYAlYMXJv")
        logging.info(
            f"{result.data.metadata.title} ({result.data.metadata.state}, {result.data.participants.total} participants)"
        )

    def test_get_use_story_topic_query(self):
        result = self.client.get_use_story_topic_query()
        for item in result.data.stories.items:
            logging.info(f"{item.trend_results.result.core.category}: {item.trend_results.result.core.name}")

    def test_get_grok_account_jwt_query(self):
        result = self.client.get_grok_account_jwt_query()
        logging.info(result.data.status)


if __name__ == "__main__":
    unittest.main()

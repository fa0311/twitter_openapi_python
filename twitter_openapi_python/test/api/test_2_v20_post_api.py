import unittest
from test.api import get_client
from urllib.parse import parse_qs, urlparse

import twitter_openapi_python as api


class TestV20PostApi(unittest.TestCase):
    client: api.V20PostApiUtils

    def setUp(self):
        self.client = get_client().get_v20_post_api()

    def test_post_timeline_feedback(self):
        timeline = get_client().get_tweet_api().get_home_timeline()
        actions = timeline.raw.response.data.data.home.home_timeline_urt.response_objects.feedback_actions
        url = next(x.value.feedback_url for x in actions if x.value.feedback_type == "DontLike")
        query = parse_qs(urlparse(url).query)
        for undo in [False, True]:
            result = self.client.post_timeline_feedback(
                feedback_type=query["feedback_type"][0],
                action_metadata=query["action_metadata"][0],
                undo=undo,
            )
            self.assertEqual(result.raw.response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

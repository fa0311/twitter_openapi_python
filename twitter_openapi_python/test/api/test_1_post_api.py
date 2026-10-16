import datetime
import unittest

import twitter_openapi_python as api
from test.api import get_client


class TestPostApi(unittest.TestCase):
    client: api.PostApiUtils

    def setUp(self):
        self.client = get_client().get_post_api()

    def test_post_create_tweet(self):
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        result = self.client.post_create_tweet(tweet_text=f"Test{time}")
        self.assertEqual(result.raw.response.status_code, 200)

    def test_post_delete_tweet(self):
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        result = self.client.post_create_tweet(tweet_text=f"Test{time}")
        assert result.data.data.create_tweet
        tweet_id = result.data.data.create_tweet.tweet_results.result.rest_id

        result2 = self.client.post_delete_tweet(tweet_id=tweet_id)
        self.assertEqual(result2.raw.response.status_code, 200)

    def test_post_create_retweet(self):
        result = self.client.post_create_retweet(tweet_id="1349129669258448897")
        self.assertEqual(result.raw.response.status_code, 200)

    def test_post_delete_retweet(self):
        result = self.client.post_delete_retweet(source_tweet_id="1349129669258448897")
        self.assertEqual(result.raw.response.status_code, 200)

    def test_post_favorite_tweet(self):
        result = self.client.post_favorite_tweet(tweet_id="1349129669258448897")
        self.assertEqual(result.raw.response.status_code, 200)

    def test_post_unfavorite_tweet(self):
        result = self.client.post_unfavorite_tweet(tweet_id="1349129669258448897")
        self.assertEqual(result.raw.response.status_code, 200)

    def test_post_create_bookmark(self):
        result = self.client.post_create_bookmark(tweet_id="1349129669258448897")
        self.assertEqual(result.raw.response.status_code, 200)

        result2 = self.client.post_delete_bookmark(tweet_id="1349129669258448897")
        self.assertEqual(result2.raw.response.status_code, 200)

    def test_post_create_list(self):
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        result = self.client.post_create_list(name=f"Test{time}", description="twitter_openapi_python", is_private=True)
        self.assertEqual(result.raw.response.status_code, 200)
        list_id = result.data.data.list.id_str

        result2 = self.client.post_list_add_member(list_id=list_id, user_id="44196397")
        self.assertEqual(result2.raw.response.status_code, 200)
        self.assertEqual(result2.data.data.list.member_count, 1)

        result3 = self.client.post_list_remove_member(list_id=list_id, user_id="44196397")
        self.assertEqual(result3.raw.response.status_code, 200)

        result4 = self.client.post_delete_list(list_id=list_id)
        self.assertEqual(result4.raw.response.status_code, 200)

    def test_post_create_draft_tweet(self):
        time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        result = self.client.post_create_draft_tweet(status=f"Test{time}")
        self.assertEqual(result.raw.response.status_code, 200)
        draft_id = result.data.data.tweet.rest_id

        result2 = self.client.post_delete_draft_tweets(draft_tweet_ids=[draft_id])
        self.assertEqual(result2.raw.response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

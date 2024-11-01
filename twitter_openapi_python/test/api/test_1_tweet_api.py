import unittest

import twitter_openapi_python as api
from test.api import get_client, print_tweet
from twitter_openapi_python.models import TweetApiUtilsData


class TestTweetApi(unittest.TestCase):
    client: api.TweetApiUtils

    def setUp(self):
        self.client = get_client().get_tweet_api()

    def ad_fillter(self, tweet: TweetApiUtilsData) -> bool:
        return tweet.promoted_metadata is None

    def test_get_tweet_detail(self):
        result = self.client.get_tweet_detail(focal_tweet_id="1349129669258448897")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def get_home_timeline(self):
        result = self.client.get_home_timeline()
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_home_latest_timeline(self):
        result = self.client.get_home_latest_timeline()
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_list_latest_tweets_timeline(self):
        result = self.client.get_list_latest_tweets_timeline(
            list_id="1141162794290520064"
        )
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_tweets(self):
        result = self.client.get_user_tweets(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_tweets_and_replies(self):
        result = self.client.get_user_tweets_and_replies(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_media(self):
        result = self.client.get_user_media(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_likes(self):
        result = self.client.get_likes(user_id="1787148517779406848")  # @ptcpz3
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_bookmarks(self):
        result = self.client.get_bookmarks()
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)


if __name__ == "__main__":
    unittest.main()

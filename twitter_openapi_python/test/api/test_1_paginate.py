import unittest

from test.api import get_client, print_tweet
from twitter_openapi_python import paginate


class TestPaginate(unittest.TestCase):
    def test_paginate_user_tweets(self):
        client = get_client().get_tweet_api()
        tweets = list(paginate(lambda cursor: client.get_user_tweets(user_id="44196397", cursor=cursor), limit=30))
        for tweet in tweets:
            print_tweet(tweet)
        self.assertEqual(len(tweets), 30)

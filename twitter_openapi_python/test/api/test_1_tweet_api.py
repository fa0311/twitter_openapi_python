import logging
import unittest

import twitter_openapi_python as api
from test.api import get_client, get_user_id, print_tweet, print_user
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
        result = self.client.get_list_latest_tweets_timeline(list_id="1141162794290520064")
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

    def test_get_user_originals_timeline(self):
        result = self.client.get_user_originals_timeline(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_replies_timeline(self):
        result = self.client.get_user_replies_timeline(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_video_timeline(self):
        result = self.client.get_user_video_timeline(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_likes(self):
        result = self.client.get_likes(user_id=get_user_id())  # only the account's own likes are visible
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_bookmarks(self):
        result = self.client.get_bookmarks()
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_community_tweets_timeline(self):
        result = self.client.get_community_tweets_timeline(community_id="1489422448332197888")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_community_media_timeline(self):
        result = self.client.get_community_media_timeline(community_id="1489422448332197888")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_highlights_tweets(self):
        result = self.client.get_user_highlights_tweets(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_reposts_timeline(self):
        result = self.client.get_user_reposts_timeline(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_user_super_follow_tweets(self):
        result = self.client.get_user_super_follow_tweets(user_id="44196397")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_explore_page(self):
        result = self.client.get_explore_page()
        for trend in result.data.data:
            logging.info(trend.name)

    def test_get_generic_timeline_by_id(self):
        timeline_id = self.client.flag["GenericTimelineById"]["variables"]["timelineId"]
        result = self.client.get_generic_timeline_by_id(timeline_id=timeline_id)
        for trend in result.data.data:
            logging.info(trend.name)

    def test_get_notifications_timeline(self):
        result = self.client.get_notifications_timeline()
        for notification in result.data.data:
            logging.info(notification.rich_message.text)

    def test_get_community_discovery_timeline(self):
        result = self.client.get_community_discovery_timeline()
        for community in result.data.data:
            logging.info(community.community.name)

    def test_get_community_about_timeline(self):
        result = self.client.get_community_about_timeline(community_id="1489422448332197888")
        for user in result.data.data:
            print_user(user)

    def test_get_connect_tab_timeline(self):
        result = self.client.get_connect_tab_timeline()
        for user in result.data.data:
            print_user(user)

    def test_get_bookmark_search_timeline(self):
        result = self.client.get_bookmark_search_timeline(raw_query="test")
        for tweet in list(filter(self.ad_fillter, result.data.data)):
            print_tweet(tweet)

    def test_get_explore_sidebar(self):
        result = self.client.get_explore_sidebar()
        for trend in result.data.data:
            logging.info(trend.name)


if __name__ == "__main__":
    unittest.main()

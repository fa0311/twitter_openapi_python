import logging
import unittest

import twitter_openapi_python as api
from test.api import get_client, print_tweet


class TestCommunityApi(unittest.TestCase):
    client: api.CommunityApiUtils

    def setUp(self):
        self.client = get_client().get_community_api()

    def test_get_communities_fetch_one_query(self):
        result = self.client.get_communities_fetch_one_query(community_id="1738874426798870555")
        logging.info(f"{result.data.name}: {result.data.member_count} members")

    def test_get_community_query(self):
        result = self.client.get_community_query(community_id="1493446837214187523")
        logging.info(f"{result.data.name}: {result.data.member_count} members")

    def test_get_communities_search_query(self):
        result = self.client.get_communities_search_query(query="test")
        for item in result.data.items_results:
            logging.info(item.result.name)

    def test_get_topic_carousel_query(self):
        result = self.client.get_topic_carousel_query()
        for topic in result.data:
            logging.info(topic.topic_name)

    def test_get_global_communities_post_search_timeline(self):
        result = self.client.get_global_communities_post_search_timeline(raw_query="test")
        for tweet in result.data.data:
            print_tweet(tweet)

    def test_get_global_communities_latest_post_search_timeline(self):
        result = self.client.get_global_communities_latest_post_search_timeline(raw_query="test")
        for tweet in result.data.data:
            print_tweet(tweet)


if __name__ == "__main__":
    unittest.main()

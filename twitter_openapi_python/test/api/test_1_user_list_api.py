import logging
import unittest
from test.api import get_client, get_user_id, print_user

import twitter_openapi_python as api


class TestUserListApi(unittest.TestCase):
    client: api.UserListApiUtils

    def setUp(self):
        self.client = get_client().get_user_list_api()

    def test_get_followers(self):
        result = self.client.get_followers(user_id="44196397")
        for user in result.data.data:
            print_user(user)

    def test_get_following(self):
        result = self.client.get_following(user_id="44196397")
        for user in result.data.data:
            print_user(user)

    def test_get_followers_you_know(self):
        result = self.client.get_followers_you_know(user_id="44196397")
        for user in result.data.data:
            print_user(user)

    def test_get_favoriters(self):
        result = self.client.get_favoriters(tweet_id="1349129669258448897")
        for user in result.data.data:
            print_user(user)

    def test_get_retweeters(self):
        result = self.client.get_retweeters(tweet_id="1349129669258448897")
        for user in result.data.data:
            print_user(user)

    def test_get_blue_verified_followers(self):
        result = self.client.get_blue_verified_followers(user_id="44196397")
        for user in result.data.data:
            print_user(user)

    def test_get_list_members(self):
        result = self.client.get_list_members(list_id="1141162794290520064")
        for user in result.data.data:
            print_user(user)

    def test_get_list_subscribers(self):
        result = self.client.get_list_subscribers(list_id="1141162794290520064")
        for user in result.data.data:
            print_user(user)

    def test_get_list_creation_recommended_users(self):
        result = self.client.get_list_creation_recommended_users(list_id="1141162794290520064")
        for user in result.data.data:
            print_user(user)

    def test_get_list_edit_recommended_users(self):
        result = self.client.get_list_edit_recommended_users(list_id="1141162794290520064")
        for user in result.data.data:
            print_user(user)

    def test_get_list_ownerships(self):
        result = self.client.get_list_ownerships(user_id=get_user_id())
        for twitter_list in result.data.data:
            logging.info(twitter_list.name)

    def test_get_list_by_rest_id(self):
        result = self.client.get_list_by_rest_id(list_id="1141162794290520064")
        logging.info(f"{result.data.name}: {result.data.member_count} members")

    def test_get_list_search_timeline(self):
        result = self.client.get_list_search_timeline(raw_query="test")
        for twitter_list in result.data.data:
            logging.info(twitter_list.name)

    def test_get_combined_lists(self):
        result = self.client.get_combined_lists(user_id="44196397")
        for twitter_list in result.data.data:
            logging.info(twitter_list.name)

    def test_get_lists_management_page_timeline(self):
        result = self.client.get_lists_management_page_timeline()
        for twitter_list in result.data.data:
            logging.info(twitter_list.name)


if __name__ == "__main__":
    unittest.main()

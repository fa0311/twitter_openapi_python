import unittest
import twitter_openapi_python as api
from test.api import get_client, print_user


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


if __name__ == "__main__":
    unittest.main()

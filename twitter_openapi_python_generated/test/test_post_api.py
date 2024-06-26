# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from twitter_openapi_python_generated.api.post_api import PostApi


class TestPostApi(unittest.TestCase):
    """PostApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PostApi()

    def tearDown(self) -> None:
        pass

    def test_post_create_bookmark(self) -> None:
        """Test case for post_create_bookmark

        """
        pass

    def test_post_create_retweet(self) -> None:
        """Test case for post_create_retweet

        """
        pass

    def test_post_create_tweet(self) -> None:
        """Test case for post_create_tweet

        """
        pass

    def test_post_delete_bookmark(self) -> None:
        """Test case for post_delete_bookmark

        """
        pass

    def test_post_delete_retweet(self) -> None:
        """Test case for post_delete_retweet

        """
        pass

    def test_post_delete_tweet(self) -> None:
        """Test case for post_delete_tweet

        """
        pass

    def test_post_favorite_tweet(self) -> None:
        """Test case for post_favorite_tweet

        """
        pass

    def test_post_unfavorite_tweet(self) -> None:
        """Test case for post_unfavorite_tweet

        """
        pass


if __name__ == '__main__':
    unittest.main()

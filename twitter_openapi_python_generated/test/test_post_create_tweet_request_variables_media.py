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

from twitter_openapi_python_generated.models.post_create_tweet_request_variables_media import PostCreateTweetRequestVariablesMedia

class TestPostCreateTweetRequestVariablesMedia(unittest.TestCase):
    """PostCreateTweetRequestVariablesMedia unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCreateTweetRequestVariablesMedia:
        """Test PostCreateTweetRequestVariablesMedia
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateTweetRequestVariablesMedia`
        """
        model = PostCreateTweetRequestVariablesMedia()
        if include_optional:
            return PostCreateTweetRequestVariablesMedia(
                media_entities = [
                    twitter_openapi_python_generated.models.post_create_tweet_request_variables_media_media_entities_inner.postCreateTweet_request_variables_media_media_entities_inner(
                        media_id = '1111111111111111111', 
                        tagged_users = [
                            '44196397'
                            ], )
                    ],
                possibly_sensitive = False
            )
        else:
            return PostCreateTweetRequestVariablesMedia(
                possibly_sensitive = False,
        )
        """

    def testPostCreateTweetRequestVariablesMedia(self):
        """Test PostCreateTweetRequestVariablesMedia"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

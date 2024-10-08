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

from twitter_openapi_python_generated.models.post_create_tweet_request_variables_reply import PostCreateTweetRequestVariablesReply

class TestPostCreateTweetRequestVariablesReply(unittest.TestCase):
    """PostCreateTweetRequestVariablesReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCreateTweetRequestVariablesReply:
        """Test PostCreateTweetRequestVariablesReply
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateTweetRequestVariablesReply`
        """
        model = PostCreateTweetRequestVariablesReply()
        if include_optional:
            return PostCreateTweetRequestVariablesReply(
                exclude_reply_user_ids = [
                    None
                    ],
                in_reply_to_tweet_id = '1111111111111111111'
            )
        else:
            return PostCreateTweetRequestVariablesReply(
                exclude_reply_user_ids = [
                    None
                    ],
                in_reply_to_tweet_id = '1111111111111111111',
        )
        """

    def testPostCreateTweetRequestVariablesReply(self):
        """Test PostCreateTweetRequestVariablesReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

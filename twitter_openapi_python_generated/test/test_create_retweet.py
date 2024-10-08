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

from twitter_openapi_python_generated.models.create_retweet import CreateRetweet

class TestCreateRetweet(unittest.TestCase):
    """CreateRetweet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRetweet:
        """Test CreateRetweet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRetweet`
        """
        model = CreateRetweet()
        if include_optional:
            return CreateRetweet(
                result = twitter_openapi_python_generated.models.retweet.Retweet(
                    legacy = twitter_openapi_python_generated.models.retweet_legacy.Retweet_legacy(
                        full_text = '', ), 
                    rest_id = '4', )
            )
        else:
            return CreateRetweet(
                result = twitter_openapi_python_generated.models.retweet.Retweet(
                    legacy = twitter_openapi_python_generated.models.retweet_legacy.Retweet_legacy(
                        full_text = '', ), 
                    rest_id = '4', ),
        )
        """

    def testCreateRetweet(self):
        """Test CreateRetweet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from twitter_openapi_python_generated.models.feedback_info import FeedbackInfo

class TestFeedbackInfo(unittest.TestCase):
    """FeedbackInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeedbackInfo:
        """Test FeedbackInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeedbackInfo`
        """
        model = FeedbackInfo()
        if include_optional:
            return FeedbackInfo(
                client_event_info = twitter_openapi_python_generated.models.client_event_info.ClientEventInfo(
                    component = '', 
                    details = { }, 
                    element = '', ),
                feedback_keys = [
                    ''
                    ]
            )
        else:
            return FeedbackInfo(
        )
        """

    def testFeedbackInfo(self):
        """Test FeedbackInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

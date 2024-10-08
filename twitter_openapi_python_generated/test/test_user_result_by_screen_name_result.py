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

from twitter_openapi_python_generated.models.user_result_by_screen_name_result import UserResultByScreenNameResult

class TestUserResultByScreenNameResult(unittest.TestCase):
    """UserResultByScreenNameResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserResultByScreenNameResult:
        """Test UserResultByScreenNameResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserResultByScreenNameResult`
        """
        model = UserResultByScreenNameResult()
        if include_optional:
            return UserResultByScreenNameResult(
                typename = 'TimelineTweet',
                id = 'G',
                legacy = twitter_openapi_python_generated.models.user_result_by_screen_name_legacy.UserResultByScreenNameLegacy(
                    blocked_by = True, 
                    blocking = True, 
                    followed_by = True, 
                    following = True, 
                    name = '', 
                    protected = True, 
                    screen_name = '', ),
                profilemodules = { },
                rest_id = '4'
            )
        else:
            return UserResultByScreenNameResult(
                typename = 'TimelineTweet',
                id = 'G',
                legacy = twitter_openapi_python_generated.models.user_result_by_screen_name_legacy.UserResultByScreenNameLegacy(
                    blocked_by = True, 
                    blocking = True, 
                    followed_by = True, 
                    following = True, 
                    name = '', 
                    protected = True, 
                    screen_name = '', ),
                profilemodules = { },
                rest_id = '4',
        )
        """

    def testUserResultByScreenNameResult(self):
        """Test UserResultByScreenNameResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

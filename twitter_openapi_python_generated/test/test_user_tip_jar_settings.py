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

from twitter_openapi_python_generated.models.user_tip_jar_settings import UserTipJarSettings

class TestUserTipJarSettings(unittest.TestCase):
    """UserTipJarSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserTipJarSettings:
        """Test UserTipJarSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserTipJarSettings`
        """
        model = UserTipJarSettings()
        if include_optional:
            return UserTipJarSettings(
                bandcamp_handle = '',
                bitcoin_handle = '',
                cash_app_handle = '',
                ethereum_handle = '',
                gofundme_handle = '',
                is_enabled = True,
                patreon_handle = '',
                pay_pal_handle = '',
                venmo_handle = ''
            )
        else:
            return UserTipJarSettings(
        )
        """

    def testUserTipJarSettings(self):
        """Test UserTipJarSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

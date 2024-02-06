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
import datetime

from twitter_openapi_python_generated.models.cover_cta import CoverCta

class TestCoverCta(unittest.TestCase):
    """CoverCta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoverCta:
        """Test CoverCta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoverCta`
        """
        model = CoverCta()
        if include_optional:
            return CoverCta(
                text = '',
                button_style = 'Primary',
                callbacks = [
                    twitter_openapi_python_generated.models.callback.Callback(
                        endpoint = '', )
                    ],
                client_event_info = twitter_openapi_python_generated.models.cta_client_event_info.CtaClientEventInfo(
                    action = 'primary_cta', ),
                cta_behavior = twitter_openapi_python_generated.models.timeline_cover_behavior.TimelineCoverBehavior(
                    type = 'TimelineCoverBehaviorDismiss', )
            )
        else:
            return CoverCta(
                callbacks = [
                    twitter_openapi_python_generated.models.callback.Callback(
                        endpoint = '', )
                    ],
                client_event_info = twitter_openapi_python_generated.models.cta_client_event_info.CtaClientEventInfo(
                    action = 'primary_cta', ),
                cta_behavior = twitter_openapi_python_generated.models.timeline_cover_behavior.TimelineCoverBehavior(
                    type = 'TimelineCoverBehaviorDismiss', ),
        )
        """

    def testCoverCta(self):
        """Test CoverCta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from twitter_openapi_python_generated.models.timeline_general_context import TimelineGeneralContext

class TestTimelineGeneralContext(unittest.TestCase):
    """TimelineGeneralContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineGeneralContext:
        """Test TimelineGeneralContext
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineGeneralContext`
        """
        model = TimelineGeneralContext()
        if include_optional:
            return TimelineGeneralContext(
                context_image_urls = [
                    ''
                    ],
                context_type = 'Follow',
                landing_url = twitter_openapi_python_generated.models.social_context_landing_url.SocialContextLandingUrl(
                    url = '', 
                    url_type = 'DeepLink', 
                    urt_endpoint_options = twitter_openapi_python_generated.models.urt_endpoint_options.UrtEndpointOptions(
                        request_params = [
                            twitter_openapi_python_generated.models.urt_endpoint_request_params.UrtEndpointRequestParams(
                                key = '', 
                                value = '', )
                            ], 
                        title = '', ), ),
                text = '',
                type = 'TimelineGeneralContext'
            )
        else:
            return TimelineGeneralContext(
        )
        """

    def testTimelineGeneralContext(self):
        """Test TimelineGeneralContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

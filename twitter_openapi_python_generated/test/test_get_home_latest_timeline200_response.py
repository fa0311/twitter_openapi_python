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

import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.get_home_latest_timeline200_response import GetHomeLatestTimeline200Response  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestGetHomeLatestTimeline200Response(unittest.TestCase):
    """GetHomeLatestTimeline200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetHomeLatestTimeline200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHomeLatestTimeline200Response`
        """
        model = twitter_openapi_python_generated.models.get_home_latest_timeline200_response.GetHomeLatestTimeline200Response()  # noqa: E501
        if include_optional :
            return GetHomeLatestTimeline200Response(
                data = twitter_openapi_python_generated.models.home_timeline_response_data.HomeTimelineResponseData(
                    home = twitter_openapi_python_generated.models.home_timeline_home.HomeTimelineHome(
                        home_timeline_urt = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), ), 
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ]
            )
        else :
            return GetHomeLatestTimeline200Response(
                data = twitter_openapi_python_generated.models.home_timeline_response_data.HomeTimelineResponseData(
                    home = twitter_openapi_python_generated.models.home_timeline_home.HomeTimelineHome(
                        home_timeline_urt = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), ),
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ],
        )
        """

    def testGetHomeLatestTimeline200Response(self):
        """Test GetHomeLatestTimeline200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

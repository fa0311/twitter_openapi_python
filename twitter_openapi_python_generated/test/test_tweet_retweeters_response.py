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

from twitter_openapi_python_generated.models.tweet_retweeters_response import TweetRetweetersResponse

class TestTweetRetweetersResponse(unittest.TestCase):
    """TweetRetweetersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetRetweetersResponse:
        """Test TweetRetweetersResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetRetweetersResponse`
        """
        model = TweetRetweetersResponse()
        if include_optional:
            return TweetRetweetersResponse(
                data = twitter_openapi_python_generated.models.tweet_retweeters_response_data.TweetRetweetersResponseData(
                    retweeters_timeline = twitter_openapi_python_generated.models.timeline_v2.TimelineV2(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), ),
                errors = [
                    twitter_openapi_python_generated.models.error_response.ErrorResponse(
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
        else:
            return TweetRetweetersResponse(
                data = twitter_openapi_python_generated.models.tweet_retweeters_response_data.TweetRetweetersResponseData(
                    retweeters_timeline = twitter_openapi_python_generated.models.timeline_v2.TimelineV2(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), ),
        )
        """

    def testTweetRetweetersResponse(self):
        """Test TweetRetweetersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

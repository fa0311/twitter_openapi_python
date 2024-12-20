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

from twitter_openapi_python_generated.models.user_highlights_tweets_response import UserHighlightsTweetsResponse

class TestUserHighlightsTweetsResponse(unittest.TestCase):
    """UserHighlightsTweetsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserHighlightsTweetsResponse:
        """Test UserHighlightsTweetsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserHighlightsTweetsResponse`
        """
        model = UserHighlightsTweetsResponse()
        if include_optional:
            return UserHighlightsTweetsResponse(
                data = twitter_openapi_python_generated.models.user_highlights_tweets_data.UserHighlightsTweetsData(
                    user = twitter_openapi_python_generated.models.user_highlights_tweets_user.UserHighlightsTweetsUser(
                        result = twitter_openapi_python_generated.models.user_highlights_tweets_result.UserHighlightsTweetsResult(
                            __typename = 'TimelineTweet', 
                            timeline = twitter_openapi_python_generated.models.user_highlights_tweets_timeline.UserHighlightsTweetsTimeline(
                                timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                                    instructions = [
                                        null
                                        ], 
                                    metadata = { }, 
                                    response_objects = { }, ), ), ), ), ),
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
                            null
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ]
            )
        else:
            return UserHighlightsTweetsResponse(
                data = twitter_openapi_python_generated.models.user_highlights_tweets_data.UserHighlightsTweetsData(
                    user = twitter_openapi_python_generated.models.user_highlights_tweets_user.UserHighlightsTweetsUser(
                        result = twitter_openapi_python_generated.models.user_highlights_tweets_result.UserHighlightsTweetsResult(
                            __typename = 'TimelineTweet', 
                            timeline = twitter_openapi_python_generated.models.user_highlights_tweets_timeline.UserHighlightsTweetsTimeline(
                                timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                                    instructions = [
                                        null
                                        ], 
                                    metadata = { }, 
                                    response_objects = { }, ), ), ), ), ),
        )
        """

    def testUserHighlightsTweetsResponse(self):
        """Test UserHighlightsTweetsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from twitter_openapi_python_generated.models.media_video_info import MediaVideoInfo

class TestMediaVideoInfo(unittest.TestCase):
    """MediaVideoInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MediaVideoInfo:
        """Test MediaVideoInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaVideoInfo`
        """
        model = MediaVideoInfo()
        if include_optional:
            return MediaVideoInfo(
                aspect_ratio = [
                    56
                    ],
                duration_millis = 56,
                variants = [
                    twitter_openapi_python_generated.models.media_video_info_variant.MediaVideoInfoVariant(
                        bitrate = 56, 
                        content_type = '', 
                        url = '', )
                    ]
            )
        else:
            return MediaVideoInfo(
                aspect_ratio = [
                    56
                    ],
                variants = [
                    twitter_openapi_python_generated.models.media_video_info_variant.MediaVideoInfoVariant(
                        bitrate = 56, 
                        content_type = '', 
                        url = '', )
                    ],
        )
        """

    def testMediaVideoInfo(self):
        """Test MediaVideoInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

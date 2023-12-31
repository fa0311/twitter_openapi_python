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
from twitter_openapi_python_generated.models.media_sizes import MediaSizes  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestMediaSizes(unittest.TestCase):
    """MediaSizes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MediaSizes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaSizes`
        """
        model = twitter_openapi_python_generated.models.media_sizes.MediaSizes()  # noqa: E501
        if include_optional :
            return MediaSizes(
                large = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ), 
                medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ), 
                small = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ), 
                thumb = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, )
            )
        else :
            return MediaSizes(
                large = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ),
                medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ),
                small = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ),
                thumb = twitter_openapi_python_generated.models.media_size.MediaSize(
                    h = 56, 
                    resize = 'crop', 
                    w = 56, ),
        )
        """

    def testMediaSizes(self):
        """Test MediaSizes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

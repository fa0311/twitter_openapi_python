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

from twitter_openapi_python_generated.models.thumbnail_image import ThumbnailImage

class TestThumbnailImage(unittest.TestCase):
    """ThumbnailImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ThumbnailImage:
        """Test ThumbnailImage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ThumbnailImage`
        """
        model = ThumbnailImage()
        if include_optional:
            return ThumbnailImage(
                original_img_height = 56,
                original_img_url = '',
                original_img_width = 56
            )
        else:
            return ThumbnailImage(
        )
        """

    def testThumbnailImage(self):
        """Test ThumbnailImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

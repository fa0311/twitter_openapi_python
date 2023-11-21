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
from twitter_openapi_python_generated.models.birdwatch_pivot_note import BirdwatchPivotNote  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestBirdwatchPivotNote(unittest.TestCase):
    """BirdwatchPivotNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BirdwatchPivotNote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BirdwatchPivotNote`
        """
        model = twitter_openapi_python_generated.models.birdwatch_pivot_note.BirdwatchPivotNote()  # noqa: E501
        if include_optional :
            return BirdwatchPivotNote(
                rest_id = '4'
            )
        else :
            return BirdwatchPivotNote(
                rest_id = '4',
        )
        """

    def testBirdwatchPivotNote(self):
        """Test BirdwatchPivotNote"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
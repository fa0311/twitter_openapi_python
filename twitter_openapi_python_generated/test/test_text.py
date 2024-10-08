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

from twitter_openapi_python_generated.models.text import Text

class TestText(unittest.TestCase):
    """Text unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Text:
        """Test Text
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Text`
        """
        model = Text()
        if include_optional:
            return Text(
                entities = [
                    twitter_openapi_python_generated.models.text_entity.TextEntity(
                        from_index = 56, 
                        ref = twitter_openapi_python_generated.models.text_entity_ref.TextEntityRef(
                            type = 'TimelineUrl', 
                            url = '', 
                            url_type = 'ExternalUrl', ), 
                        to_index = 56, )
                    ],
                text = ''
            )
        else:
            return Text(
                entities = [
                    twitter_openapi_python_generated.models.text_entity.TextEntity(
                        from_index = 56, 
                        ref = twitter_openapi_python_generated.models.text_entity_ref.TextEntityRef(
                            type = 'TimelineUrl', 
                            url = '', 
                            url_type = 'ExternalUrl', ), 
                        to_index = 56, )
                    ],
                text = '',
        )
        """

    def testText(self):
        """Test Text"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

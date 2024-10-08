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

from twitter_openapi_python_generated.models.article import Article

class TestArticle(unittest.TestCase):
    """Article unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Article:
        """Test Article
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Article`
        """
        model = Article()
        if include_optional:
            return Article(
                article_results = twitter_openapi_python_generated.models.article_results.ArticleResults(
                    result = twitter_openapi_python_generated.models.article_result.ArticleResult(
                        cover_media = twitter_openapi_python_generated.models.article_cover_media.ArticleCoverMedia(
                            id = '', 
                            media_id = '4', 
                            media_info = twitter_openapi_python_generated.models.article_cover_media_info.ArticleCoverMediaInfo(
                                __typename = 'TimelineTweet', 
                                color_info = twitter_openapi_python_generated.models.article_cover_media_color_info.ArticleCoverMediaColorInfo(
                                    palette = [
                                        twitter_openapi_python_generated.models.article_cover_media_color_info_palette.ArticleCoverMediaColorInfoPalette(
                                            percentage = 1.337, 
                                            rgb = twitter_openapi_python_generated.models.article_cover_media_color_info_palette_rgb.ArticleCoverMediaColorInfoPaletteRGB(
                                                blue = 56, 
                                                green = 56, 
                                                red = 56, ), )
                                        ], ), 
                                original_img_height = 56, 
                                original_img_url = '', 
                                original_img_width = 56, ), 
                            media_key = '', ), 
                        id = '', 
                        lifecycle_state = twitter_openapi_python_generated.models.article_lifecycle_state.ArticleLifecycleState(
                            modified_at_secs = 56, ), 
                        metadata = twitter_openapi_python_generated.models.article_metadata.ArticleMetadata(
                            first_published_at_secs = 56, ), 
                        preview_text = '', 
                        rest_id = '4', 
                        title = '', ), )
            )
        else:
            return Article(
                article_results = twitter_openapi_python_generated.models.article_results.ArticleResults(
                    result = twitter_openapi_python_generated.models.article_result.ArticleResult(
                        cover_media = twitter_openapi_python_generated.models.article_cover_media.ArticleCoverMedia(
                            id = '', 
                            media_id = '4', 
                            media_info = twitter_openapi_python_generated.models.article_cover_media_info.ArticleCoverMediaInfo(
                                __typename = 'TimelineTweet', 
                                color_info = twitter_openapi_python_generated.models.article_cover_media_color_info.ArticleCoverMediaColorInfo(
                                    palette = [
                                        twitter_openapi_python_generated.models.article_cover_media_color_info_palette.ArticleCoverMediaColorInfoPalette(
                                            percentage = 1.337, 
                                            rgb = twitter_openapi_python_generated.models.article_cover_media_color_info_palette_rgb.ArticleCoverMediaColorInfoPaletteRGB(
                                                blue = 56, 
                                                green = 56, 
                                                red = 56, ), )
                                        ], ), 
                                original_img_height = 56, 
                                original_img_url = '', 
                                original_img_width = 56, ), 
                            media_key = '', ), 
                        id = '', 
                        lifecycle_state = twitter_openapi_python_generated.models.article_lifecycle_state.ArticleLifecycleState(
                            modified_at_secs = 56, ), 
                        metadata = twitter_openapi_python_generated.models.article_metadata.ArticleMetadata(
                            first_published_at_secs = 56, ), 
                        preview_text = '', 
                        rest_id = '4', 
                        title = '', ), ),
        )
        """

    def testArticle(self):
        """Test Article"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

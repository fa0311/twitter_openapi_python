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

from twitter_openapi_python_generated.models.post_create_tweet_request import PostCreateTweetRequest

class TestPostCreateTweetRequest(unittest.TestCase):
    """PostCreateTweetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCreateTweetRequest:
        """Test PostCreateTweetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateTweetRequest`
        """
        model = PostCreateTweetRequest()
        if include_optional:
            return PostCreateTweetRequest(
                features = twitter_openapi_python_generated.models.post_create_tweet_request_features.postCreateTweet_request_features(
                    c9s_tweet_anatomy_moderator_badge_enabled = True, 
                    freedom_of_speech_not_reach_fetch_enabled = True, 
                    graphql_is_translatable_rweb_tweet_is_translatable_enabled = True, 
                    longform_notetweets_consumption_enabled = True, 
                    longform_notetweets_inline_media_enabled = True, 
                    longform_notetweets_rich_text_read_enabled = True, 
                    responsive_web_edit_tweet_api_enabled = True, 
                    responsive_web_enhance_cards_enabled = False, 
                    responsive_web_graphql_exclude_directive_enabled = True, 
                    responsive_web_graphql_skip_user_profile_image_extensions_enabled = False, 
                    responsive_web_graphql_timeline_navigation_enabled = True, 
                    responsive_web_media_download_video_enabled = False, 
                    responsive_web_twitter_article_tweet_consumption_enabled = True, 
                    rweb_video_timestamps_enabled = True, 
                    standardized_nudges_misinfo = True, 
                    tweet_awards_web_tipping_enabled = False, 
                    tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled = True, 
                    tweetypie_unmention_optimization_enabled = True, 
                    verified_phone_label_enabled = False, 
                    view_counts_everywhere_api_enabled = True, ),
                query_id = '8ED1SMuUGkOZVBEjiYUTfw',
                variables = twitter_openapi_python_generated.models.post_create_tweet_request_variables.postCreateTweet_request_variables(
                    dark_request = False, 
                    media = twitter_openapi_python_generated.models.post_create_tweet_request_variables_media.postCreateTweet_request_variables_media(
                        media_entities = [
                            twitter_openapi_python_generated.models.post_create_tweet_request_variables_media_media_entities_inner.postCreateTweet_request_variables_media_media_entities_inner(
                                media_id = '1111111111111111111', 
                                tagged_users = [
                                    None
                                    ], )
                            ], 
                        possibly_sensitive = False, ), 
                    reply = twitter_openapi_python_generated.models.post_create_tweet_request_variables_reply.postCreateTweet_request_variables_reply(
                        exclude_reply_user_ids = [
                            None
                            ], 
                        in_reply_to_tweet_id = '1111111111111111111', ), 
                    semantic_annotation_ids = [
                        None
                        ], 
                    tweet_text = 'test', )
            )
        else:
            return PostCreateTweetRequest(
                features = twitter_openapi_python_generated.models.post_create_tweet_request_features.postCreateTweet_request_features(
                    c9s_tweet_anatomy_moderator_badge_enabled = True, 
                    freedom_of_speech_not_reach_fetch_enabled = True, 
                    graphql_is_translatable_rweb_tweet_is_translatable_enabled = True, 
                    longform_notetweets_consumption_enabled = True, 
                    longform_notetweets_inline_media_enabled = True, 
                    longform_notetweets_rich_text_read_enabled = True, 
                    responsive_web_edit_tweet_api_enabled = True, 
                    responsive_web_enhance_cards_enabled = False, 
                    responsive_web_graphql_exclude_directive_enabled = True, 
                    responsive_web_graphql_skip_user_profile_image_extensions_enabled = False, 
                    responsive_web_graphql_timeline_navigation_enabled = True, 
                    responsive_web_media_download_video_enabled = False, 
                    responsive_web_twitter_article_tweet_consumption_enabled = True, 
                    rweb_video_timestamps_enabled = True, 
                    standardized_nudges_misinfo = True, 
                    tweet_awards_web_tipping_enabled = False, 
                    tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled = True, 
                    tweetypie_unmention_optimization_enabled = True, 
                    verified_phone_label_enabled = False, 
                    view_counts_everywhere_api_enabled = True, ),
                query_id = '8ED1SMuUGkOZVBEjiYUTfw',
                variables = twitter_openapi_python_generated.models.post_create_tweet_request_variables.postCreateTweet_request_variables(
                    dark_request = False, 
                    media = twitter_openapi_python_generated.models.post_create_tweet_request_variables_media.postCreateTweet_request_variables_media(
                        media_entities = [
                            twitter_openapi_python_generated.models.post_create_tweet_request_variables_media_media_entities_inner.postCreateTweet_request_variables_media_media_entities_inner(
                                media_id = '1111111111111111111', 
                                tagged_users = [
                                    None
                                    ], )
                            ], 
                        possibly_sensitive = False, ), 
                    reply = twitter_openapi_python_generated.models.post_create_tweet_request_variables_reply.postCreateTweet_request_variables_reply(
                        exclude_reply_user_ids = [
                            None
                            ], 
                        in_reply_to_tweet_id = '1111111111111111111', ), 
                    semantic_annotation_ids = [
                        None
                        ], 
                    tweet_text = 'test', ),
        )
        """

    def testPostCreateTweetRequest(self):
        """Test PostCreateTweetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

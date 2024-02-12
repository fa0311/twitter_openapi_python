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

from twitter_openapi_python_generated.models.tweet_interstitial import TweetInterstitial

class TestTweetInterstitial(unittest.TestCase):
    """TweetInterstitial unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TweetInterstitial:
        """Test TweetInterstitial
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetInterstitial`
        """
        model = TweetInterstitial()
        if include_optional:
            return TweetInterstitial(
                typename = 'TimelineTweet',
                display_type = 'NonCompliant',
                reveal_text = twitter_openapi_python_generated.models.tweet_interstitial_reveal_text.TweetInterstitialRevealText(
                    entities = [
                        twitter_openapi_python_generated.models.tweet_interstitial_text_entity.TweetInterstitialTextEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.tweet_interstitial_text_entity_ref.TweetInterstitialTextEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    rtl = True, 
                    text = '', ),
                text = twitter_openapi_python_generated.models.tweet_interstitial_text.TweetInterstitialText(
                    entities = [
                        twitter_openapi_python_generated.models.tweet_interstitial_text_entity.TweetInterstitialTextEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.tweet_interstitial_text_entity_ref.TweetInterstitialTextEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    rtl = True, 
                    text = '', )
            )
        else:
            return TweetInterstitial(
                typename = 'TimelineTweet',
                display_type = 'NonCompliant',
                reveal_text = twitter_openapi_python_generated.models.tweet_interstitial_reveal_text.TweetInterstitialRevealText(
                    entities = [
                        twitter_openapi_python_generated.models.tweet_interstitial_text_entity.TweetInterstitialTextEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.tweet_interstitial_text_entity_ref.TweetInterstitialTextEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    rtl = True, 
                    text = '', ),
                text = twitter_openapi_python_generated.models.tweet_interstitial_text.TweetInterstitialText(
                    entities = [
                        twitter_openapi_python_generated.models.tweet_interstitial_text_entity.TweetInterstitialTextEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.tweet_interstitial_text_entity_ref.TweetInterstitialTextEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    rtl = True, 
                    text = '', ),
        )
        """

    def testTweetInterstitial(self):
        """Test TweetInterstitial"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
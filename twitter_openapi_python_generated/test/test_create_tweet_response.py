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

from twitter_openapi_python_generated.models.create_tweet_response import CreateTweetResponse

class TestCreateTweetResponse(unittest.TestCase):
    """CreateTweetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTweetResponse:
        """Test CreateTweetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTweetResponse`
        """
        model = CreateTweetResponse()
        if include_optional:
            return CreateTweetResponse(
                data = twitter_openapi_python_generated.models.create_tweet_response_data.CreateTweetResponseData(
                    create_tweet = twitter_openapi_python_generated.models.create_tweet_response_result.CreateTweetResponseResult(
                        tweet_results = twitter_openapi_python_generated.models.create_tweet.CreateTweet(
                            result = twitter_openapi_python_generated.models.tweet.Tweet(
                                __typename = 'TimelineTweet', 
                                birdwatch_pivot = twitter_openapi_python_generated.models.birdwatch_pivot.BirdwatchPivot(
                                    destination_url = '', 
                                    footer = twitter_openapi_python_generated.models.birdwatch_pivot_footer.BirdwatchPivotFooter(
                                        entities = [
                                            twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                                                from_index = 56, 
                                                ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                                    type = 'TimelineUrl', 
                                                    url = '', 
                                                    url_type = 'ExternalUrl', ), 
                                                to_index = 56, )
                                            ], 
                                        text = '', ), 
                                    icon_type = 'BirdwatchV1Icon', 
                                    note = twitter_openapi_python_generated.models.birdwatch_pivot_note.BirdwatchPivotNote(
                                        rest_id = '4', ), 
                                    shorttitle = '', 
                                    subtitle = twitter_openapi_python_generated.models.birdwatch_pivot_subtitle.BirdwatchPivotSubtitle(
                                        entities = [
                                            twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                                                from_index = 56, 
                                                ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                                    type = 'TimelineUrl', 
                                                    url = '', 
                                                    url_type = 'ExternalUrl', ), 
                                                to_index = 56, )
                                            ], 
                                        text = '', ), 
                                    title = '', 
                                    visual_style = 'Default', ), 
                                card = twitter_openapi_python_generated.models.tweet_card.TweetCard(
                                    legacy = twitter_openapi_python_generated.models.tweet_card_legacy.TweetCardLegacy(
                                        binding_values = [
                                            twitter_openapi_python_generated.models.tweet_card_legacy_binding_value.TweetCardLegacyBindingValue(
                                                key = '', 
                                                value = twitter_openapi_python_generated.models.tweet_card_legacy_binding_value_data.TweetCardLegacyBindingValueData(
                                                    boolean_value = True, 
                                                    scribe_key = '', 
                                                    string_value = '', 
                                                    type = '', ), )
                                            ], 
                                        name = '', 
                                        url = '', ), 
                                    rest_id = '', ), 
                                core = twitter_openapi_python_generated.models.user_result_core.UserResultCore(
                                    user_results = twitter_openapi_python_generated.models.user_results.UserResults(), ), 
                                edit_control = twitter_openapi_python_generated.models.tweet_edit_control.TweetEditControl(
                                    edit_control_initial = twitter_openapi_python_generated.models.tweet_edit_control_initial.TweetEditControlInitial(
                                        edit_tweet_ids = [
                                            '4'
                                            ], 
                                        editable_until_msecs = '4', 
                                        edits_remaining = '4', 
                                        is_edit_eligible = True, ), 
                                    edit_tweet_ids = [
                                        '4'
                                        ], 
                                    editable_until_msecs = '4', 
                                    edits_remaining = '4', 
                                    initial_tweet_id = '4', 
                                    is_edit_eligible = True, ), 
                                edit_prespective = twitter_openapi_python_generated.models.tweet_edit_prespective.TweetEditPrespective(
                                    favorited = True, 
                                    retweeted = True, ), 
                                is_translatable = True, 
                                legacy = twitter_openapi_python_generated.models.tweet_legacy.TweetLegacy(
                                    bookmark_count = 56, 
                                    bookmarked = True, 
                                    conversation_id_str = '4', 
                                    created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                                    display_text_range = [
                                        56
                                        ], 
                                    entities = twitter_openapi_python_generated.models.entities.Entities(
                                        hashtags = [
                                            { }
                                            ], 
                                        media = [
                                            twitter_openapi_python_generated.models.media.Media(
                                                display_url = '', 
                                                expanded_url = '', 
                                                features = twitter_openapi_python_generated.models.features.features(), 
                                                id_str = '4', 
                                                indices = [
                                                    56
                                                    ], 
                                                media_url_https = '', 
                                                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                                                    focus_rects = [
                                                        twitter_openapi_python_generated.models.media_original_info_focus_rect.MediaOriginalInfoFocusRect(
                                                            h = 56, 
                                                            w = 56, 
                                                            x = 56, 
                                                            y = 56, )
                                                        ], 
                                                    height = 56, 
                                                    width = 56, ), 
                                                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                                                    large = twitter_openapi_python_generated.models.media_size.MediaSize(
                                                        h = 56, 
                                                        resize = 'crop', 
                                                        w = 56, ), 
                                                    medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                                                        h = 56, 
                                                        resize = 'crop', 
                                                        w = 56, ), 
                                                    small = , 
                                                    thumb = , ), 
                                                type = 'photo', 
                                                url = '', )
                                            ], 
                                        symbols = [
                                            { }
                                            ], 
                                        urls = [
                                            twitter_openapi_python_generated.models.url.Url(
                                                display_url = '', 
                                                expanded_url = '', 
                                                indices = [
                                                    56
                                                    ], 
                                                url = '', )
                                            ], 
                                        user_mentions = [
                                            { }
                                            ], ), 
                                    extended_entities = twitter_openapi_python_generated.models.extended_entities.ExtendedEntities(
                                        media = [
                                            twitter_openapi_python_generated.models.media_extended.MediaExtended(
                                                additional_media_info = twitter_openapi_python_generated.models.additional_media_info.AdditionalMediaInfo(
                                                    monetizable = True, ), 
                                                display_url = '', 
                                                expanded_url = '', 
                                                ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.extMediaAvailability(
                                                    reason = '', 
                                                    status = 'Available', ), 
                                                features = twitter_openapi_python_generated.models.features.features(), 
                                                id_str = '4', 
                                                indices = , 
                                                media_stats = twitter_openapi_python_generated.models.media_stats.mediaStats(
                                                    view_count = 56, ), 
                                                media_key = '', 
                                                media_url_https = '', 
                                                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                                                    height = 56, 
                                                    width = 56, ), 
                                                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                                                    large = , 
                                                    medium = , 
                                                    small = , 
                                                    thumb = , ), 
                                                type = 'photo', 
                                                url = '', 
                                                video_info = twitter_openapi_python_generated.models.media_video_info.MediaVideoInfo(
                                                    aspect_ratio = [
                                                        56
                                                        ], 
                                                    duration_millis = 56, 
                                                    variants = [
                                                        twitter_openapi_python_generated.models.media_video_info_variant.MediaVideoInfoVariant(
                                                            bitrate = 56, 
                                                            content_type = '', 
                                                            url = '', )
                                                        ], ), )
                                            ], ), 
                                    favorite_count = 56, 
                                    favorited = True, 
                                    full_text = '', 
                                    id_str = '4', 
                                    is_quote_status = True, 
                                    lang = '', 
                                    possibly_sensitive = True, 
                                    possibly_sensitive_editable = True, 
                                    quote_count = 56, 
                                    reply_count = 56, 
                                    retweet_count = 56, 
                                    retweeted = True, 
                                    retweeted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(), 
                                    self_thread = twitter_openapi_python_generated.models.self_thread.SelfThread(
                                        id_str = '4', ), 
                                    user_id_str = '4', ), 
                                note_tweet = twitter_openapi_python_generated.models.note_tweet.NoteTweet(
                                    is_expandable = True, 
                                    note_tweet_results = twitter_openapi_python_generated.models.note_tweet_result.NoteTweetResult(
                                        result = twitter_openapi_python_generated.models.note_tweet_result_data.NoteTweetResultData(
                                            entity_set = twitter_openapi_python_generated.models.entities.Entities(
                                                hashtags = [
                                                    { }
                                                    ], 
                                                symbols = [
                                                    { }
                                                    ], 
                                                urls = [
                                                    twitter_openapi_python_generated.models.url.Url(
                                                        display_url = '', 
                                                        expanded_url = '', 
                                                        indices = , 
                                                        url = '', )
                                                    ], 
                                                user_mentions = [
                                                    { }
                                                    ], ), 
                                            id = 'zA9LCSLv1C1ylmgd0/Y2TA5TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SR//=', 
                                            richtext = twitter_openapi_python_generated.models.note_tweet_result_rich_text.NoteTweetResultRichText(
                                                richtext_tags = [
                                                    twitter_openapi_python_generated.models.note_tweet_result_rich_text_tag.NoteTweetResultRichTextTag(
                                                        from_index = 56, 
                                                        richtext_types = [
                                                            'Bold'
                                                            ], 
                                                        to_index = 56, )
                                                    ], ), 
                                            text = '', ), ), ), 
                                quick_promote_eligibility = twitter_openapi_python_generated.models.quick_promote_eligibility.quick_promote_eligibility(), 
                                quoted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(), 
                                rest_id = '4', 
                                source = '', 
                                unmention_data = { }, 
                                views = twitter_openapi_python_generated.models.tweet_view.TweetView(
                                    count = '4', 
                                    state = 'EnabledWithCount', ), ), ), ), )
            )
        else:
            return CreateTweetResponse(
                data = twitter_openapi_python_generated.models.create_tweet_response_data.CreateTweetResponseData(
                    create_tweet = twitter_openapi_python_generated.models.create_tweet_response_result.CreateTweetResponseResult(
                        tweet_results = twitter_openapi_python_generated.models.create_tweet.CreateTweet(
                            result = twitter_openapi_python_generated.models.tweet.Tweet(
                                __typename = 'TimelineTweet', 
                                birdwatch_pivot = twitter_openapi_python_generated.models.birdwatch_pivot.BirdwatchPivot(
                                    destination_url = '', 
                                    footer = twitter_openapi_python_generated.models.birdwatch_pivot_footer.BirdwatchPivotFooter(
                                        entities = [
                                            twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                                                from_index = 56, 
                                                ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                                    type = 'TimelineUrl', 
                                                    url = '', 
                                                    url_type = 'ExternalUrl', ), 
                                                to_index = 56, )
                                            ], 
                                        text = '', ), 
                                    icon_type = 'BirdwatchV1Icon', 
                                    note = twitter_openapi_python_generated.models.birdwatch_pivot_note.BirdwatchPivotNote(
                                        rest_id = '4', ), 
                                    shorttitle = '', 
                                    subtitle = twitter_openapi_python_generated.models.birdwatch_pivot_subtitle.BirdwatchPivotSubtitle(
                                        entities = [
                                            twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                                                from_index = 56, 
                                                ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                                    type = 'TimelineUrl', 
                                                    url = '', 
                                                    url_type = 'ExternalUrl', ), 
                                                to_index = 56, )
                                            ], 
                                        text = '', ), 
                                    title = '', 
                                    visual_style = 'Default', ), 
                                card = twitter_openapi_python_generated.models.tweet_card.TweetCard(
                                    legacy = twitter_openapi_python_generated.models.tweet_card_legacy.TweetCardLegacy(
                                        binding_values = [
                                            twitter_openapi_python_generated.models.tweet_card_legacy_binding_value.TweetCardLegacyBindingValue(
                                                key = '', 
                                                value = twitter_openapi_python_generated.models.tweet_card_legacy_binding_value_data.TweetCardLegacyBindingValueData(
                                                    boolean_value = True, 
                                                    scribe_key = '', 
                                                    string_value = '', 
                                                    type = '', ), )
                                            ], 
                                        name = '', 
                                        url = '', ), 
                                    rest_id = '', ), 
                                core = twitter_openapi_python_generated.models.user_result_core.UserResultCore(
                                    user_results = twitter_openapi_python_generated.models.user_results.UserResults(), ), 
                                edit_control = twitter_openapi_python_generated.models.tweet_edit_control.TweetEditControl(
                                    edit_control_initial = twitter_openapi_python_generated.models.tweet_edit_control_initial.TweetEditControlInitial(
                                        edit_tweet_ids = [
                                            '4'
                                            ], 
                                        editable_until_msecs = '4', 
                                        edits_remaining = '4', 
                                        is_edit_eligible = True, ), 
                                    edit_tweet_ids = [
                                        '4'
                                        ], 
                                    editable_until_msecs = '4', 
                                    edits_remaining = '4', 
                                    initial_tweet_id = '4', 
                                    is_edit_eligible = True, ), 
                                edit_prespective = twitter_openapi_python_generated.models.tweet_edit_prespective.TweetEditPrespective(
                                    favorited = True, 
                                    retweeted = True, ), 
                                is_translatable = True, 
                                legacy = twitter_openapi_python_generated.models.tweet_legacy.TweetLegacy(
                                    bookmark_count = 56, 
                                    bookmarked = True, 
                                    conversation_id_str = '4', 
                                    created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                                    display_text_range = [
                                        56
                                        ], 
                                    entities = twitter_openapi_python_generated.models.entities.Entities(
                                        hashtags = [
                                            { }
                                            ], 
                                        media = [
                                            twitter_openapi_python_generated.models.media.Media(
                                                display_url = '', 
                                                expanded_url = '', 
                                                features = twitter_openapi_python_generated.models.features.features(), 
                                                id_str = '4', 
                                                indices = [
                                                    56
                                                    ], 
                                                media_url_https = '', 
                                                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                                                    focus_rects = [
                                                        twitter_openapi_python_generated.models.media_original_info_focus_rect.MediaOriginalInfoFocusRect(
                                                            h = 56, 
                                                            w = 56, 
                                                            x = 56, 
                                                            y = 56, )
                                                        ], 
                                                    height = 56, 
                                                    width = 56, ), 
                                                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                                                    large = twitter_openapi_python_generated.models.media_size.MediaSize(
                                                        h = 56, 
                                                        resize = 'crop', 
                                                        w = 56, ), 
                                                    medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                                                        h = 56, 
                                                        resize = 'crop', 
                                                        w = 56, ), 
                                                    small = , 
                                                    thumb = , ), 
                                                type = 'photo', 
                                                url = '', )
                                            ], 
                                        symbols = [
                                            { }
                                            ], 
                                        urls = [
                                            twitter_openapi_python_generated.models.url.Url(
                                                display_url = '', 
                                                expanded_url = '', 
                                                indices = [
                                                    56
                                                    ], 
                                                url = '', )
                                            ], 
                                        user_mentions = [
                                            { }
                                            ], ), 
                                    extended_entities = twitter_openapi_python_generated.models.extended_entities.ExtendedEntities(
                                        media = [
                                            twitter_openapi_python_generated.models.media_extended.MediaExtended(
                                                additional_media_info = twitter_openapi_python_generated.models.additional_media_info.AdditionalMediaInfo(
                                                    monetizable = True, ), 
                                                display_url = '', 
                                                expanded_url = '', 
                                                ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.extMediaAvailability(
                                                    reason = '', 
                                                    status = 'Available', ), 
                                                features = twitter_openapi_python_generated.models.features.features(), 
                                                id_str = '4', 
                                                indices = , 
                                                media_stats = twitter_openapi_python_generated.models.media_stats.mediaStats(
                                                    view_count = 56, ), 
                                                media_key = '', 
                                                media_url_https = '', 
                                                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                                                    height = 56, 
                                                    width = 56, ), 
                                                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                                                    large = , 
                                                    medium = , 
                                                    small = , 
                                                    thumb = , ), 
                                                type = 'photo', 
                                                url = '', 
                                                video_info = twitter_openapi_python_generated.models.media_video_info.MediaVideoInfo(
                                                    aspect_ratio = [
                                                        56
                                                        ], 
                                                    duration_millis = 56, 
                                                    variants = [
                                                        twitter_openapi_python_generated.models.media_video_info_variant.MediaVideoInfoVariant(
                                                            bitrate = 56, 
                                                            content_type = '', 
                                                            url = '', )
                                                        ], ), )
                                            ], ), 
                                    favorite_count = 56, 
                                    favorited = True, 
                                    full_text = '', 
                                    id_str = '4', 
                                    is_quote_status = True, 
                                    lang = '', 
                                    possibly_sensitive = True, 
                                    possibly_sensitive_editable = True, 
                                    quote_count = 56, 
                                    reply_count = 56, 
                                    retweet_count = 56, 
                                    retweeted = True, 
                                    retweeted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(), 
                                    self_thread = twitter_openapi_python_generated.models.self_thread.SelfThread(
                                        id_str = '4', ), 
                                    user_id_str = '4', ), 
                                note_tweet = twitter_openapi_python_generated.models.note_tweet.NoteTweet(
                                    is_expandable = True, 
                                    note_tweet_results = twitter_openapi_python_generated.models.note_tweet_result.NoteTweetResult(
                                        result = twitter_openapi_python_generated.models.note_tweet_result_data.NoteTweetResultData(
                                            entity_set = twitter_openapi_python_generated.models.entities.Entities(
                                                hashtags = [
                                                    { }
                                                    ], 
                                                symbols = [
                                                    { }
                                                    ], 
                                                urls = [
                                                    twitter_openapi_python_generated.models.url.Url(
                                                        display_url = '', 
                                                        expanded_url = '', 
                                                        indices = , 
                                                        url = '', )
                                                    ], 
                                                user_mentions = [
                                                    { }
                                                    ], ), 
                                            id = 'zA9LCSLv1C1ylmgd0/Y2TA5TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SR//=', 
                                            richtext = twitter_openapi_python_generated.models.note_tweet_result_rich_text.NoteTweetResultRichText(
                                                richtext_tags = [
                                                    twitter_openapi_python_generated.models.note_tweet_result_rich_text_tag.NoteTweetResultRichTextTag(
                                                        from_index = 56, 
                                                        richtext_types = [
                                                            'Bold'
                                                            ], 
                                                        to_index = 56, )
                                                    ], ), 
                                            text = '', ), ), ), 
                                quick_promote_eligibility = twitter_openapi_python_generated.models.quick_promote_eligibility.quick_promote_eligibility(), 
                                quoted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(), 
                                rest_id = '4', 
                                source = '', 
                                unmention_data = { }, 
                                views = twitter_openapi_python_generated.models.tweet_view.TweetView(
                                    count = '4', 
                                    state = 'EnabledWithCount', ), ), ), ), ),
        )
        """

    def testCreateTweetResponse(self):
        """Test CreateTweetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

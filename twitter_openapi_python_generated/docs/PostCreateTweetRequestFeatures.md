# PostCreateTweetRequestFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freedom_of_speech_not_reach_fetch_enabled** | **bool** |  | [default to True]
**graphql_is_translatable_rweb_tweet_is_translatable_enabled** | **bool** |  | [default to True]
**longform_notetweets_consumption_enabled** | **bool** |  | [default to True]
**longform_notetweets_inline_media_enabled** | **bool** |  | [default to True]
**longform_notetweets_rich_text_read_enabled** | **bool** |  | [default to True]
**responsive_web_edit_tweet_api_enabled** | **bool** |  | [default to True]
**responsive_web_enhance_cards_enabled** | **bool** |  | [default to False]
**responsive_web_graphql_exclude_directive_enabled** | **bool** |  | [default to True]
**responsive_web_graphql_skip_user_profile_image_extensions_enabled** | **bool** |  | [default to False]
**responsive_web_graphql_timeline_navigation_enabled** | **bool** |  | [default to True]
**responsive_web_media_download_video_enabled** | **bool** |  | [default to False]
**responsive_web_twitter_article_tweet_consumption_enabled** | **bool** |  | [default to False]
**standardized_nudges_misinfo** | **bool** |  | [default to True]
**tweet_awards_web_tipping_enabled** | **bool** |  | [default to False]
**tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled** | **bool** |  | [default to True]
**tweetypie_unmention_optimization_enabled** | **bool** |  | [default to True]
**verified_phone_label_enabled** | **bool** |  | [default to False]
**view_counts_everywhere_api_enabled** | **bool** |  | [default to True]

## Example

```python
from twitter_openapi_python_generated.models.post_create_tweet_request_features import PostCreateTweetRequestFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateTweetRequestFeatures from a JSON string
post_create_tweet_request_features_instance = PostCreateTweetRequestFeatures.from_json(json)
# print the JSON string representation of the object
print PostCreateTweetRequestFeatures.to_json()

# convert the object into a dict
post_create_tweet_request_features_dict = post_create_tweet_request_features_instance.to_dict()
# create an instance of PostCreateTweetRequestFeatures from a dict
post_create_tweet_request_features_form_dict = post_create_tweet_request_features.from_dict(post_create_tweet_request_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



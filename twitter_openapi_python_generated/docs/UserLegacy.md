# UserLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by** | **bool** |  | [default to False]
**blocking** | **bool** |  | [default to False]
**can_dm** | **bool** |  | [default to False]
**can_media_tag** | **bool** |  | [default to False]
**created_at** | **str** |  | 
**default_profile** | **bool** |  | [default to False]
**default_profile_image** | **bool** |  | [default to False]
**description** | **str** |  | 
**entities** | **Dict[str, object]** |  | 
**fast_followers_count** | **int** |  | 
**favourites_count** | **int** |  | [default to 0]
**follow_request_sent** | **bool** |  | [optional] [default to False]
**followed_by** | **bool** |  | [optional] [default to False]
**followers_count** | **int** |  | [default to 0]
**following** | **bool** |  | [optional] [default to False]
**friends_count** | **int** |  | [default to 0]
**has_custom_timelines** | **bool** |  | [default to False]
**is_translator** | **bool** |  | [default to False]
**listed_count** | **int** |  | [default to 0]
**location** | **str** |  | 
**media_count** | **int** |  | [default to 0]
**muting** | **bool** |  | [default to False]
**name** | **str** |  | 
**normal_followers_count** | **int** |  | [default to 0]
**notifications** | **bool** |  | [optional] [default to False]
**pinned_tweet_ids_str** | **List[str]** |  | 
**possibly_sensitive** | **bool** |  | [default to False]
**profile_banner_extensions** | **object** |  | [optional] 
**profile_banner_url** | **str** |  | [optional] 
**profile_image_extensions** | **object** |  | [optional] 
**profile_image_url_https** | **str** |  | 
**profile_interstitial_type** | **str** |  | 
**protected** | **bool** |  | [optional] [default to False]
**screen_name** | **str** |  | 
**statuses_count** | **int** |  | [default to 0]
**translator_type** | **str** |  | 
**url** | **str** |  | [optional] 
**verified** | **bool** |  | 
**verified_type** | **str** |  | [optional] 
**want_retweets** | **bool** |  | [default to False]
**withheld_in_countries** | **List[str]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_legacy import UserLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of UserLegacy from a JSON string
user_legacy_instance = UserLegacy.from_json(json)
# print the JSON string representation of the object
print(UserLegacy.to_json())

# convert the object into a dict
user_legacy_dict = user_legacy_instance.to_dict()
# create an instance of UserLegacy from a dict
user_legacy_form_dict = user_legacy.from_dict(user_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



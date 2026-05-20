# UserLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by** | **bool** |  | [optional] 
**blocking** | **bool** |  | [optional] 
**can_dm** | **bool** |  | [optional] 
**can_media_tag** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**default_profile** | **bool** |  | 
**default_profile_image** | **bool** |  | 
**description** | **str** |  | 
**entities** | **Dict[str, object]** |  | 
**fast_followers_count** | **int** |  | 
**favourites_count** | **int** |  | 
**follow_request_sent** | **bool** |  | [optional] 
**followed_by** | **bool** |  | [optional] 
**followers_count** | **int** |  | 
**following** | **bool** |  | [optional] 
**friends_count** | **int** |  | 
**has_custom_timelines** | **bool** |  | 
**is_translator** | **bool** |  | 
**listed_count** | **int** |  | 
**location** | **str** |  | [optional] 
**media_count** | **int** |  | 
**muting** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**normal_followers_count** | **int** |  | 
**notifications** | **bool** |  | [optional] 
**pinned_tweet_ids_str** | **List[str]** |  | [optional] 
**possibly_sensitive** | **bool** |  | 
**profile_banner_extensions** | **object** |  | [optional] 
**profile_banner_url** | **str** |  | [optional] 
**profile_image_extensions** | **object** |  | [optional] 
**profile_image_url_https** | **str** |  | [optional] 
**profile_interstitial_type** | **str** |  | 
**protected** | **bool** |  | [optional] 
**screen_name** | **str** |  | [optional] 
**statuses_count** | **int** |  | 
**time_zone** | **str** |  | 
**translator_type** | **str** |  | 
**url** | **str** |  | [optional] 
**utc_offset** | **int** |  | 
**verified** | **bool** |  | [optional] 
**verified_type** | **str** |  | [optional] 
**want_retweets** | **bool** |  | [optional] 
**withheld_description** | **str** |  | 
**withheld_in_countries** | **List[str]** |  | [optional] 
**withheld_scope** | **str** |  | 

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
user_legacy_from_dict = UserLegacy.from_dict(user_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



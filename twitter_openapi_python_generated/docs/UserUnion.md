# UserUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**affiliates_highlighted_label** | **Dict[str, object]** |  | [optional] 
**business_account** | **Dict[str, object]** |  | [optional] 
**creator_subscriptions_count** | **int** |  | [optional] 
**has_graduated_access** | **bool** |  | [optional] 
**has_hidden_likes_on_profile** | **bool** |  | [optional] 
**has_hidden_subscriptions_on_profile** | **bool** |  | [optional] 
**has_nft_avatar** | **bool** |  | [optional] 
**highlights_info** | [**UserHighlightsInfo**](UserHighlightsInfo.md) |  | [optional] 
**id** | **str** |  | 
**is_blue_verified** | **bool** |  | 
**is_profile_translatable** | **bool** |  | [optional] 
**legacy** | [**UserLegacy**](UserLegacy.md) |  | 
**legacy_extended_profile** | [**UserLegacyExtendedProfile**](UserLegacyExtendedProfile.md) |  | [optional] 
**premium_gifting_eligible** | **bool** |  | [optional] 
**professional** | [**UserProfessional**](UserProfessional.md) |  | [optional] 
**profile_image_shape** | **str** |  | 
**rest_id** | **str** |  | 
**super_follow_eligible** | **bool** |  | [optional] 
**super_followed_by** | **bool** |  | [optional] 
**super_following** | **bool** |  | [optional] 
**tipjar_settings** | [**UserTipJarSettings**](UserTipJarSettings.md) |  | [optional] 
**user_seed_tweet_count** | **int** |  | [optional] 
**verification_info** | [**UserVerificationInfo**](UserVerificationInfo.md) |  | [optional] 
**message** | **str** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_union import UserUnion

# TODO update the JSON string below
json = "{}"
# create an instance of UserUnion from a JSON string
user_union_instance = UserUnion.from_json(json)
# print the JSON string representation of the object
print(UserUnion.to_json())

# convert the object into a dict
user_union_dict = user_union_instance.to_dict()
# create an instance of UserUnion from a dict
user_union_from_dict = UserUnion.from_dict(user_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



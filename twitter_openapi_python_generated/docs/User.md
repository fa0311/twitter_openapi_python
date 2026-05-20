# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**affiliates_highlighted_label** | **Dict[str, object]** |  | [optional] 
**avatar** | [**UserAvatar**](UserAvatar.md) |  | [optional] 
**business_account** | **Dict[str, object]** |  | [optional] 
**core** | [**UserCore**](UserCore.md) |  | [optional] 
**creator_subscriptions_count** | **int** |  | [optional] 
**dm_permissions** | [**UserDmPermissions**](UserDmPermissions.md) |  | [optional] 
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
**location** | [**UserLocation**](UserLocation.md) |  | [optional] 
**media_permissions** | [**UserMediaPermissions**](UserMediaPermissions.md) |  | [optional] 
**parody_commentary_fan_label** | **str** |  | [optional] 
**premium_gifting_eligible** | **bool** |  | [optional] 
**privacy** | [**UserPrivacy**](UserPrivacy.md) |  | [optional] 
**professional** | [**UserProfessional**](UserProfessional.md) |  | [optional] 
**profile_bio** | [**ProfileBio**](ProfileBio.md) |  | [optional] 
**profile_description_language** | **str** |  | [optional] 
**profile_image_shape** | **str** |  | 
**profile_sort_enabled** | **bool** |  | [optional] 
**relationship_perspectives** | [**UserRelationshipPerspectives**](UserRelationshipPerspectives.md) |  | [optional] 
**rest_id** | **str** |  | 
**super_follow_eligible** | **bool** |  | [optional] 
**super_followed_by** | **bool** |  | [optional] 
**super_following** | **bool** |  | [optional] 
**super_follows_user_profile** | [**UserProfile**](UserProfile.md) |  | [optional] 
**tipjar_settings** | [**UserTipJarSettings**](UserTipJarSettings.md) |  | [optional] 
**user_seed_tweet_count** | **int** |  | [optional] 
**verification** | [**UserVerification**](UserVerification.md) |  | [optional] 
**verification_info** | [**UserVerificationInfo**](UserVerificationInfo.md) |  | [optional] 
**verified_user_profiles** | [**UserProfile**](UserProfile.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**action_counts** | [**UserActionCounts**](UserActionCounts.md) |  | [optional] 
**affiliates_highlighted_label** | **Dict[str, object]** |  | [optional] 
**avatar** | [**UserAvatar**](UserAvatar.md) |  | [optional] 
**banner** | [**UserBanner**](UserBanner.md) |  | [optional] 
**business_account** | **Dict[str, object]** |  | [optional] 
**core** | [**UserCore**](UserCore.md) |  | [optional] 
**creator_subscriptions_count** | **int** |  | [optional] 
**dm_permissions** | [**UserDmPermissions**](UserDmPermissions.md) |  | [optional] 
**follow_request_sent** | **bool** |  | [optional] 
**has_graduated_access** | **bool** |  | [optional] 
**has_hidden_likes_on_profile** | **bool** |  | [optional] 
**has_hidden_subscriptions_on_profile** | **bool** |  | [optional] 
**has_nft_avatar** | **bool** |  | [optional] 
**highlights_info** | [**UserHighlightsInfo**](UserHighlightsInfo.md) |  | [optional] 
**id** | **str** |  | 
**is_blue_verified** | **bool** |  | 
**is_profile_translatable** | **bool** |  | [optional] 
**is_verified_organization** | **bool** |  | [optional] 
**legacy** | [**UserLegacy**](UserLegacy.md) |  | [optional] 
**legacy_extended_profile** | [**UserLegacyExtendedProfile**](UserLegacyExtendedProfile.md) |  | [optional] 
**location** | [**UserLocation**](UserLocation.md) |  | [optional] 
**media_permissions** | [**UserMediaPermissions**](UserMediaPermissions.md) |  | [optional] 
**notifications_settings** | [**UserNotificationsSettings**](UserNotificationsSettings.md) |  | [optional] 
**parody_commentary_fan_label** | **str** |  | [optional] 
**pinned_items** | [**UserPinnedItems**](UserPinnedItems.md) |  | [optional] 
**possibly_sensitive** | **bool** |  | [optional] 
**premium_gifting_eligible** | **bool** |  | [optional] 
**privacy** | [**UserPrivacy**](UserPrivacy.md) |  | [optional] 
**professional** | [**UserProfessional**](UserProfessional.md) |  | [optional] 
**profile_bio** | [**ProfileBio**](ProfileBio.md) |  | [optional] 
**profile_description_language** | **str** |  | [optional] 
**profile_image_shape** | **str** |  | 
**profile_metadata** | [**UserProfileMetadata**](UserProfileMetadata.md) |  | [optional] 
**profile_sort_enabled** | **bool** |  | [optional] 
**profile_translation** | [**UserProfileTranslation**](UserProfileTranslation.md) |  | [optional] 
**relationship_counts** | [**UserRelationshipCounts**](UserRelationshipCounts.md) |  | [optional] 
**relationship_perspectives** | [**UserRelationshipPerspectives**](UserRelationshipPerspectives.md) |  | [optional] 
**rest_id** | **str** |  | 
**super_follow_eligible** | **bool** |  | [optional] 
**super_followed_by** | **bool** |  | [optional] 
**super_following** | **bool** |  | [optional] 
**super_follows_user_profile** | [**UserProfile**](UserProfile.md) |  | [optional] 
**tipjar_settings** | [**UserTipJarSettings**](UserTipJarSettings.md) |  | [optional] 
**tweet_counts** | [**UserTweetCounts**](UserTweetCounts.md) |  | [optional] 
**user_seed_tweet_count** | **int** |  | [optional] 
**verification** | [**UserVerification**](UserVerification.md) |  | [optional] 
**verification_info** | [**UserVerificationInfo**](UserVerificationInfo.md) |  | [optional] 
**verified_user_profiles** | [**UserProfile**](UserProfile.md) |  | [optional] 
**website** | [**UserWebsite**](UserWebsite.md) |  | [optional] 
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



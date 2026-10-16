# CommunitySettingsCommunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**actions** | [**CommunitySettingsActions**](CommunitySettingsActions.md) |  | 
**created_at** | **int** |  | 
**creator_results** | [**CommunitySettingsCreatorResults**](CommunitySettingsCreatorResults.md) |  | 
**custom_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | 
**default_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**invites_result** | [**CommunitySettingsInvitesResult**](CommunitySettingsInvitesResult.md) |  | 
**is_member** | **bool** |  | 
**is_nsfw** | **bool** |  | 
**join_policy** | **str** |  | 
**join_requests_result** | [**CommunityJoinRequestsResult**](CommunityJoinRequestsResult.md) |  | 
**member_count** | **int** |  | 
**members_facepile_results** | [**List[CommunityFacepileUserResults]**](CommunityFacepileUserResults.md) |  | 
**name** | **str** |  | 
**primary_community_topic** | [**CommunityPrimaryTopicName**](CommunityPrimaryTopicName.md) |  | 
**rest_id** | **str** |  | 
**role** | **str** |  | 
**rules** | [**List[CommunityRelayRule]**](CommunityRelayRule.md) |  | 
**trending_hashtags_slice** | [**CommunityHashtagSlice**](CommunityHashtagSlice.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_settings_community import CommunitySettingsCommunity

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySettingsCommunity from a JSON string
community_settings_community_instance = CommunitySettingsCommunity.from_json(json)
# print the JSON string representation of the object
print(CommunitySettingsCommunity.to_json())

# convert the object into a dict
community_settings_community_dict = community_settings_community_instance.to_dict()
# create an instance of CommunitySettingsCommunity from a dict
community_settings_community_from_dict = CommunitySettingsCommunity.from_dict(community_settings_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



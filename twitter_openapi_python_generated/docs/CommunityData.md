# CommunityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**actions** | [**CommunityActions**](CommunityActions.md) |  | 
**admin_results** | [**UserResults**](UserResults.md) |  | 
**created_at** | **int** |  | [optional] 
**creator_results** | [**UserResults**](UserResults.md) |  | 
**custom_banner_media** | **Dict[str, object]** |  | [optional] 
**default_banner_media** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | 
**id_str** | **str** |  | 
**invites_policy** | **str** |  | 
**invites_result** | [**CommunityInvitesResult**](CommunityInvitesResult.md) |  | 
**is_pinned** | **bool** |  | 
**join_policy** | **str** |  | 
**join_requests_result** | [**CommunityJoinRequestsResult**](CommunityJoinRequestsResult.md) |  | [optional] 
**member_count** | **int** |  | 
**members_facepile_results** | [**List[UserResults]**](UserResults.md) |  | 
**moderator_count** | **int** |  | 
**name** | **str** |  | 
**primary_community_topic** | [**PrimaryCommunityTopic**](PrimaryCommunityTopic.md) |  | [optional] 
**question** | **str** |  | [optional] 
**role** | **str** |  | 
**rules** | [**List[CommunityRule]**](CommunityRule.md) |  | 
**search_tags** | **List[str]** |  | 
**show_only_users_to_display** | **List[str]** |  | [optional] 
**urls** | [**CommunityUrls**](CommunityUrls.md) |  | [optional] 
**viewer_relationship** | **Dict[str, object]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_data import CommunityData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityData from a JSON string
community_data_instance = CommunityData.from_json(json)
# print the JSON string representation of the object
print(CommunityData.to_json())

# convert the object into a dict
community_data_dict = community_data_instance.to_dict()
# create an instance of CommunityData from a dict
community_data_from_dict = CommunityData.from_dict(community_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



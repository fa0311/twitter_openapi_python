# CommunityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**actions** | [**CommunityActions**](CommunityActions.md) |  | [optional] 
**admin_results** | [**UserResults**](UserResults.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**creator_results** | [**UserResults**](UserResults.md) |  | [optional] 
**custom_banner_media** | **Dict[str, object]** |  | [optional] 
**default_banner_media** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**id_str** | **str** |  | 
**invites_policy** | **str** |  | [optional] 
**invites_result** | [**CommunityInvitesResult**](CommunityInvitesResult.md) |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**join_policy** | **str** |  | [optional] 
**join_requests_result** | [**CommunityJoinRequestsResult**](CommunityJoinRequestsResult.md) |  | [optional] 
**member_count** | **int** |  | [optional] 
**members_facepile_results** | [**List[UserResults]**](UserResults.md) |  | [optional] 
**moderator_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**primary_community_topic** | [**PrimaryCommunityTopic**](PrimaryCommunityTopic.md) |  | [optional] 
**question** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**rules** | [**List[CommunityRule]**](CommunityRule.md) |  | [optional] 
**search_tags** | **List[str]** |  | [optional] 
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



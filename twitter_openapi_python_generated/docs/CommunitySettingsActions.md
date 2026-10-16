# CommunitySettingsActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**join_action_result** | [**CommunityJoinActionResultUnion**](CommunityJoinActionResultUnion.md) |  | 
**list_members_action_result** | [**CommunityListMembersActionResult**](CommunityListMembersActionResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_settings_actions import CommunitySettingsActions

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySettingsActions from a JSON string
community_settings_actions_instance = CommunitySettingsActions.from_json(json)
# print the JSON string representation of the object
print(CommunitySettingsActions.to_json())

# convert the object into a dict
community_settings_actions_dict = community_settings_actions_instance.to_dict()
# create an instance of CommunitySettingsActions from a dict
community_settings_actions_from_dict = CommunitySettingsActions.from_dict(community_settings_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



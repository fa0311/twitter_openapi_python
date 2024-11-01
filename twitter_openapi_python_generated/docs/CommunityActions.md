# CommunityActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_action_result** | [**CommunityDeleteActionResult**](CommunityDeleteActionResult.md) |  | [optional] 
**join_action_result** | [**CommunityJoinActionResult**](CommunityJoinActionResult.md) |  | [optional] 
**leave_action_result** | [**CommunityLeaveActionResult**](CommunityLeaveActionResult.md) |  | [optional] 
**pin_action_result** | [**CommunityPinActionResult**](CommunityPinActionResult.md) |  | [optional] 
**unpin_action_result** | [**CommunityUnpinActionResult**](CommunityUnpinActionResult.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_actions import CommunityActions

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityActions from a JSON string
community_actions_instance = CommunityActions.from_json(json)
# print the JSON string representation of the object
print(CommunityActions.to_json())

# convert the object into a dict
community_actions_dict = community_actions_instance.to_dict()
# create an instance of CommunityActions from a dict
community_actions_from_dict = CommunityActions.from_dict(community_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



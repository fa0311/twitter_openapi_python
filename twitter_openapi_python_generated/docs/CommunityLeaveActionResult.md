# CommunityLeaveActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_leave_action_result import CommunityLeaveActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityLeaveActionResult from a JSON string
community_leave_action_result_instance = CommunityLeaveActionResult.from_json(json)
# print the JSON string representation of the object
print(CommunityLeaveActionResult.to_json())

# convert the object into a dict
community_leave_action_result_dict = community_leave_action_result_instance.to_dict()
# create an instance of CommunityLeaveActionResult from a dict
community_leave_action_result_from_dict = CommunityLeaveActionResult.from_dict(community_leave_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommunityPageActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_action_result** | [**CommunityPageDeleteActionResult**](CommunityPageDeleteActionResult.md) |  | 
**id** | **str** |  | 
**join_action_result** | [**CommunityPageJoinActionResult**](CommunityPageJoinActionResult.md) |  | 
**leave_action_result** | [**CommunityPageLeaveActionResult**](CommunityPageLeaveActionResult.md) |  | 
**pin_action_result** | [**CommunityPagePinActionResult**](CommunityPagePinActionResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_actions import CommunityPageActions

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageActions from a JSON string
community_page_actions_instance = CommunityPageActions.from_json(json)
# print the JSON string representation of the object
print(CommunityPageActions.to_json())

# convert the object into a dict
community_page_actions_dict = community_page_actions_instance.to_dict()
# create an instance of CommunityPageActions from a dict
community_page_actions_from_dict = CommunityPageActions.from_dict(community_page_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



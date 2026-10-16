# CommunityPageDeleteActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_community_delete_action_result** | **str** |  | 
**typename** | [**TypeName**](TypeName.md) |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_delete_action_result import CommunityPageDeleteActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageDeleteActionResult from a JSON string
community_page_delete_action_result_instance = CommunityPageDeleteActionResult.from_json(json)
# print the JSON string representation of the object
print(CommunityPageDeleteActionResult.to_json())

# convert the object into a dict
community_page_delete_action_result_dict = community_page_delete_action_result_instance.to_dict()
# create an instance of CommunityPageDeleteActionResult from a dict
community_page_delete_action_result_from_dict = CommunityPageDeleteActionResult.from_dict(community_page_delete_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



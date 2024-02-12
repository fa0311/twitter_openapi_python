# CommunityDeleteActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_delete_action_result import CommunityDeleteActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityDeleteActionResult from a JSON string
community_delete_action_result_instance = CommunityDeleteActionResult.from_json(json)
# print the JSON string representation of the object
print CommunityDeleteActionResult.to_json()

# convert the object into a dict
community_delete_action_result_dict = community_delete_action_result_instance.to_dict()
# create an instance of CommunityDeleteActionResult from a dict
community_delete_action_result_form_dict = community_delete_action_result.from_dict(community_delete_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



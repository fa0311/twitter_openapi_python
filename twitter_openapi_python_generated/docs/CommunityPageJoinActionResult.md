# CommunityPageJoinActionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_community_join_action_result** | **str** |  | 
**typename** | [**TypeName**](TypeName.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_join_action_result import CommunityPageJoinActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageJoinActionResult from a JSON string
community_page_join_action_result_instance = CommunityPageJoinActionResult.from_json(json)
# print the JSON string representation of the object
print(CommunityPageJoinActionResult.to_json())

# convert the object into a dict
community_page_join_action_result_dict = community_page_join_action_result_instance.to_dict()
# create an instance of CommunityPageJoinActionResult from a dict
community_page_join_action_result_from_dict = CommunityPageJoinActionResult.from_dict(community_page_join_action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



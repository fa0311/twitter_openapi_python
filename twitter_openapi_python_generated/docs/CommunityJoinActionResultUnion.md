# CommunityJoinActionResultUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_join_action_result_union import CommunityJoinActionResultUnion

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityJoinActionResultUnion from a JSON string
community_join_action_result_union_instance = CommunityJoinActionResultUnion.from_json(json)
# print the JSON string representation of the object
print(CommunityJoinActionResultUnion.to_json())

# convert the object into a dict
community_join_action_result_union_dict = community_join_action_result_union_instance.to_dict()
# create an instance of CommunityJoinActionResultUnion from a dict
community_join_action_result_union_from_dict = CommunityJoinActionResultUnion.from_dict(community_join_action_result_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



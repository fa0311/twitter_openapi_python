# CommunityJoinActionUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_join_action_union import CommunityJoinActionUnion

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityJoinActionUnion from a JSON string
community_join_action_union_instance = CommunityJoinActionUnion.from_json(json)
# print the JSON string representation of the object
print(CommunityJoinActionUnion.to_json())

# convert the object into a dict
community_join_action_union_dict = community_join_action_union_instance.to_dict()
# create an instance of CommunityJoinActionUnion from a dict
community_join_action_union_from_dict = CommunityJoinActionUnion.from_dict(community_join_action_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



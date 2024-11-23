# CommunityJoinActionUnavailable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_join_action_unavailable import CommunityJoinActionUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityJoinActionUnavailable from a JSON string
community_join_action_unavailable_instance = CommunityJoinActionUnavailable.from_json(json)
# print the JSON string representation of the object
print(CommunityJoinActionUnavailable.to_json())

# convert the object into a dict
community_join_action_unavailable_dict = community_join_action_unavailable_instance.to_dict()
# create an instance of CommunityJoinActionUnavailable from a dict
community_join_action_unavailable_from_dict = CommunityJoinActionUnavailable.from_dict(community_join_action_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



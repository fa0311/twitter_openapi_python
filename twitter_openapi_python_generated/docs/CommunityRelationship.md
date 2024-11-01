# CommunityRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**CommunityActions**](CommunityActions.md) |  | 
**id** | **str** |  | 
**moderation_state** | **Dict[str, object]** |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_relationship import CommunityRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityRelationship from a JSON string
community_relationship_instance = CommunityRelationship.from_json(json)
# print the JSON string representation of the object
print(CommunityRelationship.to_json())

# convert the object into a dict
community_relationship_dict = community_relationship_instance.to_dict()
# create an instance of CommunityRelationship from a dict
community_relationship_from_dict = CommunityRelationship.from_dict(community_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



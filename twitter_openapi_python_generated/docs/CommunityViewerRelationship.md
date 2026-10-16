# CommunityViewerRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**moderation_state** | [**CommunityModerationState**](CommunityModerationState.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_viewer_relationship import CommunityViewerRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityViewerRelationship from a JSON string
community_viewer_relationship_instance = CommunityViewerRelationship.from_json(json)
# print the JSON string representation of the object
print(CommunityViewerRelationship.to_json())

# convert the object into a dict
community_viewer_relationship_dict = community_viewer_relationship_instance.to_dict()
# create an instance of CommunityViewerRelationship from a dict
community_viewer_relationship_from_dict = CommunityViewerRelationship.from_dict(community_viewer_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



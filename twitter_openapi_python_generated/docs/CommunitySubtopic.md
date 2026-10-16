# CommunitySubtopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **str** |  | 
**topic_name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_subtopic import CommunitySubtopic

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySubtopic from a JSON string
community_subtopic_instance = CommunitySubtopic.from_json(json)
# print the JSON string representation of the object
print(CommunitySubtopic.to_json())

# convert the object into a dict
community_subtopic_dict = community_subtopic_instance.to_dict()
# create an instance of CommunitySubtopic from a dict
community_subtopic_from_dict = CommunitySubtopic.from_dict(community_subtopic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



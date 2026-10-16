# CommunityTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtopics** | [**List[CommunitySubtopic]**](CommunitySubtopic.md) |  | 
**topic_id** | **str** |  | 
**topic_name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_topic import CommunityTopic

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityTopic from a JSON string
community_topic_instance = CommunityTopic.from_json(json)
# print the JSON string representation of the object
print(CommunityTopic.to_json())

# convert the object into a dict
community_topic_dict = community_topic_instance.to_dict()
# create an instance of CommunityTopic from a dict
community_topic_from_dict = CommunityTopic.from_dict(community_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



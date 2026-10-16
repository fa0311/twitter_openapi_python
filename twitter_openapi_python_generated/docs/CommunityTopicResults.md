# CommunityTopicResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_topics** | [**List[CommunityTopic]**](CommunityTopic.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_topic_results import CommunityTopicResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityTopicResults from a JSON string
community_topic_results_instance = CommunityTopicResults.from_json(json)
# print the JSON string representation of the object
print(CommunityTopicResults.to_json())

# convert the object into a dict
community_topic_results_dict = community_topic_results_instance.to_dict()
# create an instance of CommunityTopicResults from a dict
community_topic_results_from_dict = CommunityTopicResults.from_dict(community_topic_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



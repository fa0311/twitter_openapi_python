# PrimaryCommunityTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **str** |  | 
**topic_name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.primary_community_topic import PrimaryCommunityTopic

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryCommunityTopic from a JSON string
primary_community_topic_instance = PrimaryCommunityTopic.from_json(json)
# print the JSON string representation of the object
print(PrimaryCommunityTopic.to_json())

# convert the object into a dict
primary_community_topic_dict = primary_community_topic_instance.to_dict()
# create an instance of PrimaryCommunityTopic from a dict
primary_community_topic_form_dict = primary_community_topic.from_dict(primary_community_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



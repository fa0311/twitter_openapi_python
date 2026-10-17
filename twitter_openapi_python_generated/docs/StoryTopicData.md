# StoryTopicData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**story_topic** | [**StoryTopic**](StoryTopic.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.story_topic_data import StoryTopicData

# TODO update the JSON string below
json = "{}"
# create an instance of StoryTopicData from a JSON string
story_topic_data_instance = StoryTopicData.from_json(json)
# print the JSON string representation of the object
print(StoryTopicData.to_json())

# convert the object into a dict
story_topic_data_dict = story_topic_data_instance.to_dict()
# create an instance of StoryTopicData from a dict
story_topic_data_from_dict = StoryTopicData.from_dict(story_topic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



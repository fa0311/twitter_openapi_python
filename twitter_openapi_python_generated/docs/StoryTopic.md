# StoryTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**stories** | [**StoryTopicStories**](StoryTopicStories.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.story_topic import StoryTopic

# TODO update the JSON string below
json = "{}"
# create an instance of StoryTopic from a JSON string
story_topic_instance = StoryTopic.from_json(json)
# print the JSON string representation of the object
print(StoryTopic.to_json())

# convert the object into a dict
story_topic_dict = story_topic_instance.to_dict()
# create an instance of StoryTopic from a dict
story_topic_from_dict = StoryTopic.from_dict(story_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



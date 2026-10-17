# StoryTopicItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trend_results** | [**AiTrendResults**](AiTrendResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.story_topic_item import StoryTopicItem

# TODO update the JSON string below
json = "{}"
# create an instance of StoryTopicItem from a JSON string
story_topic_item_instance = StoryTopicItem.from_json(json)
# print the JSON string representation of the object
print(StoryTopicItem.to_json())

# convert the object into a dict
story_topic_item_dict = story_topic_item_instance.to_dict()
# create an instance of StoryTopicItem from a dict
story_topic_item_from_dict = StoryTopicItem.from_dict(story_topic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



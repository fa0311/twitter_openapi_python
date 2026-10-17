# StoryTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoryTopicData**](StoryTopicData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.story_topic_response import StoryTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoryTopicResponse from a JSON string
story_topic_response_instance = StoryTopicResponse.from_json(json)
# print the JSON string representation of the object
print(StoryTopicResponse.to_json())

# convert the object into a dict
story_topic_response_dict = story_topic_response_instance.to_dict()
# create an instance of StoryTopicResponse from a dict
story_topic_response_from_dict = StoryTopicResponse.from_dict(story_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



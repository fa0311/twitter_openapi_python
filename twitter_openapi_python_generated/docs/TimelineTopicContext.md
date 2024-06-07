# TimelineTopicContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functionality_type** | **str** |  | [optional] 
**topic** | [**TopicContext**](TopicContext.md) |  | [optional] 
**type** | [**SocialContextUnionType**](SocialContextUnionType.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_topic_context import TimelineTopicContext

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTopicContext from a JSON string
timeline_topic_context_instance = TimelineTopicContext.from_json(json)
# print the JSON string representation of the object
print(TimelineTopicContext.to_json())

# convert the object into a dict
timeline_topic_context_dict = timeline_topic_context_instance.to_dict()
# create an instance of TimelineTopicContext from a dict
timeline_topic_context_from_dict = TimelineTopicContext.from_dict(timeline_topic_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



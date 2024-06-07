# TopicContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**following** | **bool** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**not_interested** | **bool** |  | [optional] 
**topic_id** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.topic_context import TopicContext

# TODO update the JSON string below
json = "{}"
# create an instance of TopicContext from a JSON string
topic_context_instance = TopicContext.from_json(json)
# print the JSON string representation of the object
print(TopicContext.to_json())

# convert the object into a dict
topic_context_dict = topic_context_instance.to_dict()
# create an instance of TopicContext from a dict
topic_context_from_dict = TopicContext.from_dict(topic_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



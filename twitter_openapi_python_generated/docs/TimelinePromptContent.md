# TimelinePromptContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation** | **str** |  | 
**content_type** | **str** |  | 
**display_type** | **str** |  | 
**is_relevant_callback** | [**TimelinePromptCallback**](TimelinePromptCallback.md) |  | 
**is_relevant_text** | **str** |  | 
**not_relevant_callback** | [**TimelinePromptCallback**](TimelinePromptCallback.md) |  | 
**not_relevant_text** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_prompt_content import TimelinePromptContent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelinePromptContent from a JSON string
timeline_prompt_content_instance = TimelinePromptContent.from_json(json)
# print the JSON string representation of the object
print(TimelinePromptContent.to_json())

# convert the object into a dict
timeline_prompt_content_dict = timeline_prompt_content_instance.to_dict()
# create an instance of TimelinePromptContent from a dict
timeline_prompt_content_from_dict = TimelinePromptContent.from_dict(timeline_prompt_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



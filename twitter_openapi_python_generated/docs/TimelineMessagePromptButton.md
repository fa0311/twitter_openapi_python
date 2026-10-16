# TimelineMessagePromptButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TimelineMessagePromptButtonAction**](TimelineMessagePromptButtonAction.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_message_prompt_button import TimelineMessagePromptButton

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineMessagePromptButton from a JSON string
timeline_message_prompt_button_instance = TimelineMessagePromptButton.from_json(json)
# print the JSON string representation of the object
print(TimelineMessagePromptButton.to_json())

# convert the object into a dict
timeline_message_prompt_button_dict = timeline_message_prompt_button_instance.to_dict()
# create an instance of TimelineMessagePromptButton from a dict
timeline_message_prompt_button_from_dict = TimelineMessagePromptButton.from_dict(timeline_message_prompt_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



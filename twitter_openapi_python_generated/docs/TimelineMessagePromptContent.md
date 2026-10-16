# TimelineMessagePromptContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_rich_text** | [**TimelineMessagePromptRichText**](TimelineMessagePromptRichText.md) |  | [optional] 
**body_text** | **str** |  | [optional] 
**content_type** | **str** |  | 
**header_text** | **str** |  | 
**primary_button_action** | [**TimelineMessagePromptButton**](TimelineMessagePromptButton.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_message_prompt_content import TimelineMessagePromptContent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineMessagePromptContent from a JSON string
timeline_message_prompt_content_instance = TimelineMessagePromptContent.from_json(json)
# print the JSON string representation of the object
print(TimelineMessagePromptContent.to_json())

# convert the object into a dict
timeline_message_prompt_content_dict = timeline_message_prompt_content_instance.to_dict()
# create an instance of TimelineMessagePromptContent from a dict
timeline_message_prompt_content_from_dict = TimelineMessagePromptContent.from_dict(timeline_message_prompt_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimelineMessagePromptRichText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[TimelineMessagePromptRichTextEntity]**](TimelineMessagePromptRichTextEntity.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_message_prompt_rich_text import TimelineMessagePromptRichText

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineMessagePromptRichText from a JSON string
timeline_message_prompt_rich_text_instance = TimelineMessagePromptRichText.from_json(json)
# print the JSON string representation of the object
print(TimelineMessagePromptRichText.to_json())

# convert the object into a dict
timeline_message_prompt_rich_text_dict = timeline_message_prompt_rich_text_instance.to_dict()
# create an instance of TimelineMessagePromptRichText from a dict
timeline_message_prompt_rich_text_from_dict = TimelineMessagePromptRichText.from_dict(timeline_message_prompt_rich_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



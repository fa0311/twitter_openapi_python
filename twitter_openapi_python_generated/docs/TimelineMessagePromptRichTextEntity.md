# TimelineMessagePromptRichTextEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**TimelineMessagePromptRichTextEntityRef**](TimelineMessagePromptRichTextEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_message_prompt_rich_text_entity import TimelineMessagePromptRichTextEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineMessagePromptRichTextEntity from a JSON string
timeline_message_prompt_rich_text_entity_instance = TimelineMessagePromptRichTextEntity.from_json(json)
# print the JSON string representation of the object
print(TimelineMessagePromptRichTextEntity.to_json())

# convert the object into a dict
timeline_message_prompt_rich_text_entity_dict = timeline_message_prompt_rich_text_entity_instance.to_dict()
# create an instance of TimelineMessagePromptRichTextEntity from a dict
timeline_message_prompt_rich_text_entity_from_dict = TimelineMessagePromptRichTextEntity.from_dict(timeline_message_prompt_rich_text_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



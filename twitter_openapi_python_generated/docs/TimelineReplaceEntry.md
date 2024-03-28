# TimelineReplaceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**TimelineAddEntry**](TimelineAddEntry.md) |  | 
**entry_id_to_replace** | **str** |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_replace_entry import TimelineReplaceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineReplaceEntry from a JSON string
timeline_replace_entry_instance = TimelineReplaceEntry.from_json(json)
# print the JSON string representation of the object
print(TimelineReplaceEntry.to_json())

# convert the object into a dict
timeline_replace_entry_dict = timeline_replace_entry_instance.to_dict()
# create an instance of TimelineReplaceEntry from a dict
timeline_replace_entry_form_dict = timeline_replace_entry.from_dict(timeline_replace_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



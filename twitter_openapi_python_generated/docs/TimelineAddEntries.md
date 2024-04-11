# TimelineAddEntries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TimelineAddEntry]**](TimelineAddEntry.md) |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_add_entries import TimelineAddEntries

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineAddEntries from a JSON string
timeline_add_entries_instance = TimelineAddEntries.from_json(json)
# print the JSON string representation of the object
print(TimelineAddEntries.to_json())

# convert the object into a dict
timeline_add_entries_dict = timeline_add_entries_instance.to_dict()
# create an instance of TimelineAddEntries from a dict
timeline_add_entries_form_dict = timeline_add_entries.from_dict(timeline_add_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



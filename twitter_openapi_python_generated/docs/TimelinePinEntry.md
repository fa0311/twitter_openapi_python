# TimelinePinEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**TimelineAddEntry**](TimelineAddEntry.md) |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_pin_entry import TimelinePinEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimelinePinEntry from a JSON string
timeline_pin_entry_instance = TimelinePinEntry.from_json(json)
# print the JSON string representation of the object
print(TimelinePinEntry.to_json())

# convert the object into a dict
timeline_pin_entry_dict = timeline_pin_entry_instance.to_dict()
# create an instance of TimelinePinEntry from a dict
timeline_pin_entry_form_dict = timeline_pin_entry.from_dict(timeline_pin_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



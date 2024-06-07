# TimelineAddEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ContentUnion**](ContentUnion.md) |  | 
**entry_id** | **str** |  | 
**sort_index** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_add_entry import TimelineAddEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineAddEntry from a JSON string
timeline_add_entry_instance = TimelineAddEntry.from_json(json)
# print the JSON string representation of the object
print(TimelineAddEntry.to_json())

# convert the object into a dict
timeline_add_entry_dict = timeline_add_entry_instance.to_dict()
# create an instance of TimelineAddEntry from a dict
timeline_add_entry_from_dict = TimelineAddEntry.from_dict(timeline_add_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



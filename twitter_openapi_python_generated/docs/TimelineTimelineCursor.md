# TimelineTimelineCursor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**cursor_type** | [**CursorType**](CursorType.md) |  | 
**entry_type** | [**ContentEntryType**](ContentEntryType.md) |  | [optional] 
**item_type** | [**ContentEntryType**](ContentEntryType.md) |  | [optional] 
**value** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_timeline_cursor import TimelineTimelineCursor

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTimelineCursor from a JSON string
timeline_timeline_cursor_instance = TimelineTimelineCursor.from_json(json)
# print the JSON string representation of the object
print TimelineTimelineCursor.to_json()

# convert the object into a dict
timeline_timeline_cursor_dict = timeline_timeline_cursor_instance.to_dict()
# create an instance of TimelineTimelineCursor from a dict
timeline_timeline_cursor_form_dict = timeline_timeline_cursor.from_dict(timeline_timeline_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



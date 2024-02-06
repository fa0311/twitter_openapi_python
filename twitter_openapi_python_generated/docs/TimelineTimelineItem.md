# TimelineTimelineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | [optional] 
**entry_type** | [**ContentEntryType**](ContentEntryType.md) |  | 
**feedback_info** | **Dict[str, object]** |  | [optional] 
**item_content** | [**ItemContentUnion**](ItemContentUnion.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_timeline_item import TimelineTimelineItem

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTimelineItem from a JSON string
timeline_timeline_item_instance = TimelineTimelineItem.from_json(json)
# print the JSON string representation of the object
print TimelineTimelineItem.to_json()

# convert the object into a dict
timeline_timeline_item_dict = timeline_timeline_item_instance.to_dict()
# create an instance of TimelineTimelineItem from a dict
timeline_timeline_item_form_dict = timeline_timeline_item.from_dict(timeline_timeline_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



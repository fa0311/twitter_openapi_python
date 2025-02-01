# TimelineTimelineModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | 
**display_type** | [**DisplayType**](DisplayType.md) |  | 
**entry_type** | [**ContentEntryType**](ContentEntryType.md) |  | 
**feedback_info** | [**FeedbackInfo**](FeedbackInfo.md) |  | [optional] 
**footer** | **Dict[str, object]** |  | [optional] 
**header** | **Dict[str, object]** |  | [optional] 
**items** | [**List[ModuleItem]**](ModuleItem.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_timeline_module import TimelineTimelineModule

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTimelineModule from a JSON string
timeline_timeline_module_instance = TimelineTimelineModule.from_json(json)
# print the JSON string representation of the object
print(TimelineTimelineModule.to_json())

# convert the object into a dict
timeline_timeline_module_dict = timeline_timeline_module_instance.to_dict()
# create an instance of TimelineTimelineModule from a dict
timeline_timeline_module_from_dict = TimelineTimelineModule.from_dict(timeline_timeline_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



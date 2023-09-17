# TimelineShowCover


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | 
**cover** | [**TimelineHalfCover**](TimelineHalfCover.md) |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_show_cover import TimelineShowCover

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineShowCover from a JSON string
timeline_show_cover_instance = TimelineShowCover.from_json(json)
# print the JSON string representation of the object
print TimelineShowCover.to_json()

# convert the object into a dict
timeline_show_cover_dict = timeline_show_cover_instance.to_dict()
# create an instance of TimelineShowCover from a dict
timeline_show_cover_form_dict = timeline_show_cover.from_dict(timeline_show_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



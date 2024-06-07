# TimelineTerminateTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_terminate_timeline import TimelineTerminateTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTerminateTimeline from a JSON string
timeline_terminate_timeline_instance = TimelineTerminateTimeline.from_json(json)
# print the JSON string representation of the object
print(TimelineTerminateTimeline.to_json())

# convert the object into a dict
timeline_terminate_timeline_dict = timeline_terminate_timeline_instance.to_dict()
# create an instance of TimelineTerminateTimeline from a dict
timeline_terminate_timeline_from_dict = TimelineTerminateTimeline.from_dict(timeline_terminate_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



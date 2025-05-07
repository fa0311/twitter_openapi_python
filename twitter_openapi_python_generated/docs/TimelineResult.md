# TimelineResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timeline** | [**Timeline**](Timeline.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_result import TimelineResult

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineResult from a JSON string
timeline_result_instance = TimelineResult.from_json(json)
# print the JSON string representation of the object
print(TimelineResult.to_json())

# convert the object into a dict
timeline_result_dict = timeline_result_instance.to_dict()
# create an instance of TimelineResult from a dict
timeline_result_from_dict = TimelineResult.from_dict(timeline_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



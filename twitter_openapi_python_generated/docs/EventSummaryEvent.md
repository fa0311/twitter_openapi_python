# EventSummaryEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.event_summary_event import EventSummaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EventSummaryEvent from a JSON string
event_summary_event_instance = EventSummaryEvent.from_json(json)
# print the JSON string representation of the object
print(EventSummaryEvent.to_json())

# convert the object into a dict
event_summary_event_dict = event_summary_event_instance.to_dict()
# create an instance of EventSummaryEvent from a dict
event_summary_event_from_dict = EventSummaryEvent.from_dict(event_summary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



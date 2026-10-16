# TimelineResponseObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_actions** | [**List[FeedbackActionEntry]**](FeedbackActionEntry.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_response_objects import TimelineResponseObjects

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineResponseObjects from a JSON string
timeline_response_objects_instance = TimelineResponseObjects.from_json(json)
# print the JSON string representation of the object
print(TimelineResponseObjects.to_json())

# convert the object into a dict
timeline_response_objects_dict = timeline_response_objects_instance.to_dict()
# create an instance of TimelineResponseObjects from a dict
timeline_response_objects_from_dict = TimelineResponseObjects.from_dict(timeline_response_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



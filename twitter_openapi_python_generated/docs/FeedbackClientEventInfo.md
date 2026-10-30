# FeedbackClientEventInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**element** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.feedback_client_event_info import FeedbackClientEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackClientEventInfo from a JSON string
feedback_client_event_info_instance = FeedbackClientEventInfo.from_json(json)
# print the JSON string representation of the object
print(FeedbackClientEventInfo.to_json())

# convert the object into a dict
feedback_client_event_info_dict = feedback_client_event_info_instance.to_dict()
# create an instance of FeedbackClientEventInfo from a dict
feedback_client_event_info_from_dict = FeedbackClientEventInfo.from_dict(feedback_client_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



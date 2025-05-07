# NotificationsTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NotificationsTimelineData**](NotificationsTimelineData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.notifications_timeline_response import NotificationsTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsTimelineResponse from a JSON string
notifications_timeline_response_instance = NotificationsTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationsTimelineResponse.to_json())

# convert the object into a dict
notifications_timeline_response_dict = notifications_timeline_response_instance.to_dict()
# create an instance of NotificationsTimelineResponse from a dict
notifications_timeline_response_from_dict = NotificationsTimelineResponse.from_dict(notifications_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



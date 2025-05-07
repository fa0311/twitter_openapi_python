# NotificationsTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer_v2** | [**NotificationsViewerV2**](NotificationsViewerV2.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.notifications_timeline_data import NotificationsTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsTimelineData from a JSON string
notifications_timeline_data_instance = NotificationsTimelineData.from_json(json)
# print the JSON string representation of the object
print(NotificationsTimelineData.to_json())

# convert the object into a dict
notifications_timeline_data_dict = notifications_timeline_data_instance.to_dict()
# create an instance of NotificationsTimelineData from a dict
notifications_timeline_data_from_dict = NotificationsTimelineData.from_dict(notifications_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



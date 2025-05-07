# NotificationsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**notification_timeline** | [**TimelineResult**](TimelineResult.md) |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.notifications_result import NotificationsResult

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsResult from a JSON string
notifications_result_instance = NotificationsResult.from_json(json)
# print the JSON string representation of the object
print(NotificationsResult.to_json())

# convert the object into a dict
notifications_result_dict = notifications_result_instance.to_dict()
# create an instance of NotificationsResult from a dict
notifications_result_from_dict = NotificationsResult.from_dict(notifications_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



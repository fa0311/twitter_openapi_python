# NotificationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impression_id** | **str** |  | 
**metadata** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.notification_details import NotificationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetails from a JSON string
notification_details_instance = NotificationDetails.from_json(json)
# print the JSON string representation of the object
print(NotificationDetails.to_json())

# convert the object into a dict
notification_details_dict = notification_details_instance.to_dict()
# create an instance of NotificationDetails from a dict
notification_details_from_dict = NotificationDetails.from_dict(notification_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



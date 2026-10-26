# NotificationUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**url_type** | **str** |  | 
**urt_endpoint_options** | [**NotificationUrtEndpointOptions**](NotificationUrtEndpointOptions.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.notification_url import NotificationUrl

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUrl from a JSON string
notification_url_instance = NotificationUrl.from_json(json)
# print the JSON string representation of the object
print(NotificationUrl.to_json())

# convert the object into a dict
notification_url_dict = notification_url_instance.to_dict()
# create an instance of NotificationUrl from a dict
notification_url_from_dict = NotificationUrl.from_dict(notification_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



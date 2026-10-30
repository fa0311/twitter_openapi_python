# NotificationUrtEndpointOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_id** | **str** |  | 
**subtitle** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.notification_urt_endpoint_options import NotificationUrtEndpointOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUrtEndpointOptions from a JSON string
notification_urt_endpoint_options_instance = NotificationUrtEndpointOptions.from_json(json)
# print the JSON string representation of the object
print(NotificationUrtEndpointOptions.to_json())

# convert the object into a dict
notification_urt_endpoint_options_dict = notification_urt_endpoint_options_instance.to_dict()
# create an instance of NotificationUrtEndpointOptions from a dict
notification_urt_endpoint_options_from_dict = NotificationUrtEndpointOptions.from_dict(notification_urt_endpoint_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



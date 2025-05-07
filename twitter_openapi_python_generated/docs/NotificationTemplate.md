# NotificationTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**from_users** | **List[object]** |  | [optional] 
**target_objects** | **List[object]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.notification_template import NotificationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplate from a JSON string
notification_template_instance = NotificationTemplate.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplate.to_json())

# convert the object into a dict
notification_template_dict = notification_template_instance.to_dict()
# create an instance of NotificationTemplate from a dict
notification_template_from_dict = NotificationTemplate.from_dict(notification_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



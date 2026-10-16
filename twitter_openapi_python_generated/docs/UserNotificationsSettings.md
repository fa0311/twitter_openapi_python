# UserNotificationsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications_enabled** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_notifications_settings import UserNotificationsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotificationsSettings from a JSON string
user_notifications_settings_instance = UserNotificationsSettings.from_json(json)
# print the JSON string representation of the object
print(UserNotificationsSettings.to_json())

# convert the object into a dict
user_notifications_settings_dict = user_notifications_settings_instance.to_dict()
# create an instance of UserNotificationsSettings from a dict
user_notifications_settings_from_dict = UserNotificationsSettings.from_dict(user_notifications_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



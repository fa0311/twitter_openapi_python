# UserTipJarSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandcamp_handle** | **str** |  | [optional] 
**bitcoin_handle** | **str** |  | [optional] 
**cash_app_handle** | **str** |  | [optional] 
**ethereum_handle** | **str** |  | [optional] 
**gofundme_handle** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**patreon_handle** | **str** |  | [optional] 
**venmo_handle** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_tip_jar_settings import UserTipJarSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserTipJarSettings from a JSON string
user_tip_jar_settings_instance = UserTipJarSettings.from_json(json)
# print the JSON string representation of the object
print(UserTipJarSettings.to_json())

# convert the object into a dict
user_tip_jar_settings_dict = user_tip_jar_settings_instance.to_dict()
# create an instance of UserTipJarSettings from a dict
user_tip_jar_settings_from_dict = UserTipJarSettings.from_dict(user_tip_jar_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



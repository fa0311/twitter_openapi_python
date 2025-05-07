# NotificationsUserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**NotificationsResult**](NotificationsResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.notifications_user_results import NotificationsUserResults

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUserResults from a JSON string
notifications_user_results_instance = NotificationsUserResults.from_json(json)
# print the JSON string representation of the object
print(NotificationsUserResults.to_json())

# convert the object into a dict
notifications_user_results_dict = notifications_user_results_instance.to_dict()
# create an instance of NotificationsUserResults from a dict
notifications_user_results_from_dict = NotificationsUserResults.from_dict(notifications_user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



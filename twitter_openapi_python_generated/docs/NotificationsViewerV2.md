# NotificationsViewerV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_results** | [**NotificationsUserResults**](NotificationsUserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.notifications_viewer_v2 import NotificationsViewerV2

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsViewerV2 from a JSON string
notifications_viewer_v2_instance = NotificationsViewerV2.from_json(json)
# print the JSON string representation of the object
print(NotificationsViewerV2.to_json())

# convert the object into a dict
notifications_viewer_v2_dict = notifications_viewer_v2_instance.to_dict()
# create an instance of NotificationsViewerV2 from a dict
notifications_viewer_v2_from_dict = NotificationsViewerV2.from_dict(notifications_viewer_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



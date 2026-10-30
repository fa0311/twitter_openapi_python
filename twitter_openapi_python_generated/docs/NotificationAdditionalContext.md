# NotificationAdditionalContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**entities** | **List[object]** |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.notification_additional_context import NotificationAdditionalContext

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAdditionalContext from a JSON string
notification_additional_context_instance = NotificationAdditionalContext.from_json(json)
# print the JSON string representation of the object
print(NotificationAdditionalContext.to_json())

# convert the object into a dict
notification_additional_context_dict = notification_additional_context_instance.to_dict()
# create an instance of NotificationAdditionalContext from a dict
notification_additional_context_from_dict = NotificationAdditionalContext.from_dict(notification_additional_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



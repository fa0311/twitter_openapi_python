# LimitedAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**prompt** | [**CtaLimitedActionPrompt**](CtaLimitedActionPrompt.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.limited_action import LimitedAction

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedAction from a JSON string
limited_action_instance = LimitedAction.from_json(json)
# print the JSON string representation of the object
print(LimitedAction.to_json())

# convert the object into a dict
limited_action_dict = limited_action_instance.to_dict()
# create an instance of LimitedAction from a dict
limited_action_from_dict = LimitedAction.from_dict(limited_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



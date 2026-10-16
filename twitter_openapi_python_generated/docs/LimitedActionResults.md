# LimitedActionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_actions** | [**List[LimitedAction]**](LimitedAction.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.limited_action_results import LimitedActionResults

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedActionResults from a JSON string
limited_action_results_instance = LimitedActionResults.from_json(json)
# print the JSON string representation of the object
print(LimitedActionResults.to_json())

# convert the object into a dict
limited_action_results_dict = limited_action_results_instance.to_dict()
# create an instance of LimitedActionResults from a dict
limited_action_results_from_dict = LimitedActionResults.from_dict(limited_action_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



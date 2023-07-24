# UserResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**User**](User.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_results import UserResults

# TODO update the JSON string below
json = "{}"
# create an instance of UserResults from a JSON string
user_results_instance = UserResults.from_json(json)
# print the JSON string representation of the object
print UserResults.to_json()

# convert the object into a dict
user_results_dict = user_results_instance.to_dict()
# create an instance of UserResults from a dict
user_results_form_dict = user_results.from_dict(user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserResults**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_response_data import UserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseData from a JSON string
user_response_data_instance = UserResponseData.from_json(json)
# print the JSON string representation of the object
print UserResponseData.to_json()

# convert the object into a dict
user_response_data_dict = user_response_data_instance.to_dict()
# create an instance of UserResponseData from a dict
user_response_data_form_dict = user_response_data.from_dict(user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



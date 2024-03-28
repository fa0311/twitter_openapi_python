# UsersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserResults]**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.users_response_data import UsersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersResponseData from a JSON string
users_response_data_instance = UsersResponseData.from_json(json)
# print the JSON string representation of the object
print(UsersResponseData.to_json())

# convert the object into a dict
users_response_data_dict = users_response_data_instance.to_dict()
# create an instance of UsersResponseData from a dict
users_response_data_form_dict = users_response_data.from_dict(users_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



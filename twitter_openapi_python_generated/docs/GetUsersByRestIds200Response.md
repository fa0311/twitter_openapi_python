# GetUsersByRestIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersResponseData**](UsersResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_users_by_rest_ids200_response import GetUsersByRestIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersByRestIds200Response from a JSON string
get_users_by_rest_ids200_response_instance = GetUsersByRestIds200Response.from_json(json)
# print the JSON string representation of the object
print(GetUsersByRestIds200Response.to_json())

# convert the object into a dict
get_users_by_rest_ids200_response_dict = get_users_by_rest_ids200_response_instance.to_dict()
# create an instance of GetUsersByRestIds200Response from a dict
get_users_by_rest_ids200_response_from_dict = GetUsersByRestIds200Response.from_dict(get_users_by_rest_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



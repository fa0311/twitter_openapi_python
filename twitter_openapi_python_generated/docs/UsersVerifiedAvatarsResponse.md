# UsersVerifiedAvatarsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsersVerifiedAvatarsResponseData**](UsersVerifiedAvatarsResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.users_verified_avatars_response import UsersVerifiedAvatarsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersVerifiedAvatarsResponse from a JSON string
users_verified_avatars_response_instance = UsersVerifiedAvatarsResponse.from_json(json)
# print the JSON string representation of the object
print(UsersVerifiedAvatarsResponse.to_json())

# convert the object into a dict
users_verified_avatars_response_dict = users_verified_avatars_response_instance.to_dict()
# create an instance of UsersVerifiedAvatarsResponse from a dict
users_verified_avatars_response_from_dict = UsersVerifiedAvatarsResponse.from_dict(users_verified_avatars_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UsersVerifiedAvatarsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_results** | [**List[VerifiedAvatarUserResults]**](VerifiedAvatarUserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.users_verified_avatars_response_data import UsersVerifiedAvatarsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersVerifiedAvatarsResponseData from a JSON string
users_verified_avatars_response_data_instance = UsersVerifiedAvatarsResponseData.from_json(json)
# print the JSON string representation of the object
print(UsersVerifiedAvatarsResponseData.to_json())

# convert the object into a dict
users_verified_avatars_response_data_dict = users_verified_avatars_response_data_instance.to_dict()
# create an instance of UsersVerifiedAvatarsResponseData from a dict
users_verified_avatars_response_data_from_dict = UsersVerifiedAvatarsResponseData.from_dict(users_verified_avatars_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



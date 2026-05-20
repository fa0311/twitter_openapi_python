# UserVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**verified_type** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_verification import UserVerification

# TODO update the JSON string below
json = "{}"
# create an instance of UserVerification from a JSON string
user_verification_instance = UserVerification.from_json(json)
# print the JSON string representation of the object
print(UserVerification.to_json())

# convert the object into a dict
user_verification_dict = user_verification_instance.to_dict()
# create an instance of UserVerification from a dict
user_verification_from_dict = UserVerification.from_dict(user_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserVerificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_identity_verified** | **bool** |  | [default to False]
**reason** | [**UserVerificationInfoReason**](UserVerificationInfoReason.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_verification_info import UserVerificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserVerificationInfo from a JSON string
user_verification_info_instance = UserVerificationInfo.from_json(json)
# print the JSON string representation of the object
print UserVerificationInfo.to_json()

# convert the object into a dict
user_verification_info_dict = user_verification_info_instance.to_dict()
# create an instance of UserVerificationInfo from a dict
user_verification_info_form_dict = user_verification_info.from_dict(user_verification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



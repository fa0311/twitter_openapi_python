# UserVerificationInfoReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**UserVerificationInfoReasonDescription**](UserVerificationInfoReasonDescription.md) |  | 
**override_verified_year** | **int** |  | 
**verified_since_msec** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_verification_info_reason import UserVerificationInfoReason

# TODO update the JSON string below
json = "{}"
# create an instance of UserVerificationInfoReason from a JSON string
user_verification_info_reason_instance = UserVerificationInfoReason.from_json(json)
# print the JSON string representation of the object
print(UserVerificationInfoReason.to_json())

# convert the object into a dict
user_verification_info_reason_dict = user_verification_info_reason_instance.to_dict()
# create an instance of UserVerificationInfoReason from a dict
user_verification_info_reason_from_dict = UserVerificationInfoReason.from_dict(user_verification_info_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



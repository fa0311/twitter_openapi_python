# AboutAccountVerificationInfoReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_verified_year** | **int** |  | [optional] 
**verified_since_msec** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_account_verification_info_reason import AboutAccountVerificationInfoReason

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountVerificationInfoReason from a JSON string
about_account_verification_info_reason_instance = AboutAccountVerificationInfoReason.from_json(json)
# print the JSON string representation of the object
print(AboutAccountVerificationInfoReason.to_json())

# convert the object into a dict
about_account_verification_info_reason_dict = about_account_verification_info_reason_instance.to_dict()
# create an instance of AboutAccountVerificationInfoReason from a dict
about_account_verification_info_reason_from_dict = AboutAccountVerificationInfoReason.from_dict(about_account_verification_info_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



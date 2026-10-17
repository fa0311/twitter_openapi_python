# AboutAccountVerificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reason** | [**AboutAccountVerificationInfoReason**](AboutAccountVerificationInfoReason.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_account_verification_info import AboutAccountVerificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountVerificationInfo from a JSON string
about_account_verification_info_instance = AboutAccountVerificationInfo.from_json(json)
# print the JSON string representation of the object
print(AboutAccountVerificationInfo.to_json())

# convert the object into a dict
about_account_verification_info_dict = about_account_verification_info_instance.to_dict()
# create an instance of AboutAccountVerificationInfo from a dict
about_account_verification_info_from_dict = AboutAccountVerificationInfo.from_dict(about_account_verification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



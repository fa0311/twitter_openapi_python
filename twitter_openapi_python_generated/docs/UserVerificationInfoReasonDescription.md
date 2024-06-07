# UserVerificationInfoReasonDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[UserVerificationInfoReasonDescriptionEntities]**](UserVerificationInfoReasonDescriptionEntities.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_verification_info_reason_description import UserVerificationInfoReasonDescription

# TODO update the JSON string below
json = "{}"
# create an instance of UserVerificationInfoReasonDescription from a JSON string
user_verification_info_reason_description_instance = UserVerificationInfoReasonDescription.from_json(json)
# print the JSON string representation of the object
print(UserVerificationInfoReasonDescription.to_json())

# convert the object into a dict
user_verification_info_reason_description_dict = user_verification_info_reason_description_instance.to_dict()
# create an instance of UserVerificationInfoReasonDescription from a dict
user_verification_info_reason_description_from_dict = UserVerificationInfoReasonDescription.from_dict(user_verification_info_reason_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



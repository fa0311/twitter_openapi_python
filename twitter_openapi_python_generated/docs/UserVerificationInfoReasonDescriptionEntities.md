# UserVerificationInfoReasonDescriptionEntities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**UserVerificationInfoReasonDescriptionEntitiesRef**](UserVerificationInfoReasonDescriptionEntitiesRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_verification_info_reason_description_entities import UserVerificationInfoReasonDescriptionEntities

# TODO update the JSON string below
json = "{}"
# create an instance of UserVerificationInfoReasonDescriptionEntities from a JSON string
user_verification_info_reason_description_entities_instance = UserVerificationInfoReasonDescriptionEntities.from_json(json)
# print the JSON string representation of the object
print(UserVerificationInfoReasonDescriptionEntities.to_json())

# convert the object into a dict
user_verification_info_reason_description_entities_dict = user_verification_info_reason_description_entities_instance.to_dict()
# create an instance of UserVerificationInfoReasonDescriptionEntities from a dict
user_verification_info_reason_description_entities_form_dict = user_verification_info_reason_description_entities.from_dict(user_verification_info_reason_description_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



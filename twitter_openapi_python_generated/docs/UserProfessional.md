# UserProfessional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**List[UserProfessionalCategory]**](UserProfessionalCategory.md) |  | 
**professional_type** | **str** |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_professional import UserProfessional

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfessional from a JSON string
user_professional_instance = UserProfessional.from_json(json)
# print the JSON string representation of the object
print UserProfessional.to_json()

# convert the object into a dict
user_professional_dict = user_professional_instance.to_dict()
# create an instance of UserProfessional from a dict
user_professional_form_dict = user_professional.from_dict(user_professional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



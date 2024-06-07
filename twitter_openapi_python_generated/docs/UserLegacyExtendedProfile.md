# UserLegacyExtendedProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | [**UserLegacyExtendedProfileBirthdate**](UserLegacyExtendedProfileBirthdate.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_legacy_extended_profile import UserLegacyExtendedProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserLegacyExtendedProfile from a JSON string
user_legacy_extended_profile_instance = UserLegacyExtendedProfile.from_json(json)
# print the JSON string representation of the object
print(UserLegacyExtendedProfile.to_json())

# convert the object into a dict
user_legacy_extended_profile_dict = user_legacy_extended_profile_instance.to_dict()
# create an instance of UserLegacyExtendedProfile from a dict
user_legacy_extended_profile_from_dict = UserLegacyExtendedProfile.from_dict(user_legacy_extended_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



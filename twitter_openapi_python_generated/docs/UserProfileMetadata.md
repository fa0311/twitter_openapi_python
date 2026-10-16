# UserProfileMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_interstitial_type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_profile_metadata import UserProfileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileMetadata from a JSON string
user_profile_metadata_instance = UserProfileMetadata.from_json(json)
# print the JSON string representation of the object
print(UserProfileMetadata.to_json())

# convert the object into a dict
user_profile_metadata_dict = user_profile_metadata_instance.to_dict()
# create an instance of UserProfileMetadata from a dict
user_profile_metadata_from_dict = UserProfileMetadata.from_dict(user_profile_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



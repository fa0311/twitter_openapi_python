# AboutProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_based_in** | **str** |  | 
**affiliate_username** | **str** |  | 
**learn_more_url** | **str** |  | 
**location_accurate** | **bool** |  | 
**source** | **str** |  | 
**username_changes** | [**AboutProfileUsernameChanges**](AboutProfileUsernameChanges.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_profile import AboutProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AboutProfile from a JSON string
about_profile_instance = AboutProfile.from_json(json)
# print the JSON string representation of the object
print(AboutProfile.to_json())

# convert the object into a dict
about_profile_dict = about_profile_instance.to_dict()
# create an instance of AboutProfile from a dict
about_profile_from_dict = AboutProfile.from_dict(about_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



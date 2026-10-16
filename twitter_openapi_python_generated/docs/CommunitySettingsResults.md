# CommunitySettingsResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**CommunitySettingsCommunity**](CommunitySettingsCommunity.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_settings_results import CommunitySettingsResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySettingsResults from a JSON string
community_settings_results_instance = CommunitySettingsResults.from_json(json)
# print the JSON string representation of the object
print(CommunitySettingsResults.to_json())

# convert the object into a dict
community_settings_results_dict = community_settings_results_instance.to_dict()
# create an instance of CommunitySettingsResults from a dict
community_settings_results_from_dict = CommunitySettingsResults.from_dict(community_settings_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommunitySettingsCreatorResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**CommunitySettingsCreator**](CommunitySettingsCreator.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_settings_creator_results import CommunitySettingsCreatorResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySettingsCreatorResults from a JSON string
community_settings_creator_results_instance = CommunitySettingsCreatorResults.from_json(json)
# print the JSON string representation of the object
print(CommunitySettingsCreatorResults.to_json())

# convert the object into a dict
community_settings_creator_results_dict = community_settings_creator_results_instance.to_dict()
# create an instance of CommunitySettingsCreatorResults from a dict
community_settings_creator_results_from_dict = CommunitySettingsCreatorResults.from_dict(community_settings_creator_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



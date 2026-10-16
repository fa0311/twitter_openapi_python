# CommunitySettingsCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**core** | [**CommunitySettingsCreatorCore**](CommunitySettingsCreatorCore.md) |  | 
**id** | **str** |  | 
**is_blue_verified** | **bool** |  | 
**verification** | [**CommunitySettingsCreatorVerification**](CommunitySettingsCreatorVerification.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_settings_creator import CommunitySettingsCreator

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySettingsCreator from a JSON string
community_settings_creator_instance = CommunitySettingsCreator.from_json(json)
# print the JSON string representation of the object
print(CommunitySettingsCreator.to_json())

# convert the object into a dict
community_settings_creator_dict = community_settings_creator_instance.to_dict()
# create an instance of CommunitySettingsCreator from a dict
community_settings_creator_from_dict = CommunitySettingsCreator.from_dict(community_settings_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



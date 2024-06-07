# AdditionalMediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_to_actions** | [**AdditionalMediaInfoCallToActions**](AdditionalMediaInfoCallToActions.md) |  | [optional] 
**description** | **str** |  | [optional] 
**embeddable** | **bool** |  | [optional] 
**monetizable** | **bool** |  | 
**source_user** | [**UserResultCore**](UserResultCore.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.additional_media_info import AdditionalMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalMediaInfo from a JSON string
additional_media_info_instance = AdditionalMediaInfo.from_json(json)
# print the JSON string representation of the object
print(AdditionalMediaInfo.to_json())

# convert the object into a dict
additional_media_info_dict = additional_media_info_instance.to_dict()
# create an instance of AdditionalMediaInfo from a dict
additional_media_info_from_dict = AdditionalMediaInfo.from_dict(additional_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



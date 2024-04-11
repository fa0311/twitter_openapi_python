# UserResultByScreenNameLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by** | **bool** |  | [optional] 
**blocking** | **bool** |  | [optional] 
**followed_by** | **bool** |  | [optional] 
**following** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 
**screen_name** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_result_by_screen_name_legacy import UserResultByScreenNameLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultByScreenNameLegacy from a JSON string
user_result_by_screen_name_legacy_instance = UserResultByScreenNameLegacy.from_json(json)
# print the JSON string representation of the object
print(UserResultByScreenNameLegacy.to_json())

# convert the object into a dict
user_result_by_screen_name_legacy_dict = user_result_by_screen_name_legacy_instance.to_dict()
# create an instance of UserResultByScreenNameLegacy from a dict
user_result_by_screen_name_legacy_form_dict = user_result_by_screen_name_legacy.from_dict(user_result_by_screen_name_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



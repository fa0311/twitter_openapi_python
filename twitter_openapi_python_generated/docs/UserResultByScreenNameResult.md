# UserResultByScreenNameResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**id** | **str** |  | 
**legacy** | [**UserResultByScreenNameLegacy**](UserResultByScreenNameLegacy.md) |  | 
**profilemodules** | **Dict[str, object]** |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_result_by_screen_name_result import UserResultByScreenNameResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultByScreenNameResult from a JSON string
user_result_by_screen_name_result_instance = UserResultByScreenNameResult.from_json(json)
# print the JSON string representation of the object
print UserResultByScreenNameResult.to_json()

# convert the object into a dict
user_result_by_screen_name_result_dict = user_result_by_screen_name_result_instance.to_dict()
# create an instance of UserResultByScreenNameResult from a dict
user_result_by_screen_name_result_form_dict = user_result_by_screen_name_result.from_dict(user_result_by_screen_name_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



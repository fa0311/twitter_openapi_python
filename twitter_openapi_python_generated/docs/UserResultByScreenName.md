# UserResultByScreenName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**UserResultByScreenNameResult**](UserResultByScreenNameResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_result_by_screen_name import UserResultByScreenName

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultByScreenName from a JSON string
user_result_by_screen_name_instance = UserResultByScreenName.from_json(json)
# print the JSON string representation of the object
print(UserResultByScreenName.to_json())

# convert the object into a dict
user_result_by_screen_name_dict = user_result_by_screen_name_instance.to_dict()
# create an instance of UserResultByScreenName from a dict
user_result_by_screen_name_from_dict = UserResultByScreenName.from_dict(user_result_by_screen_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



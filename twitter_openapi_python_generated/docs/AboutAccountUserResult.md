# AboutAccountUserResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**AboutAccountUser**](AboutAccountUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_account_user_result import AboutAccountUserResult

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountUserResult from a JSON string
about_account_user_result_instance = AboutAccountUserResult.from_json(json)
# print the JSON string representation of the object
print(AboutAccountUserResult.to_json())

# convert the object into a dict
about_account_user_result_dict = about_account_user_result_instance.to_dict()
# create an instance of AboutAccountUserResult from a dict
about_account_user_result_from_dict = AboutAccountUserResult.from_dict(about_account_user_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



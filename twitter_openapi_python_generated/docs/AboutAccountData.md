# AboutAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_result_by_screen_name** | [**AboutAccountUserResult**](AboutAccountUserResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.about_account_data import AboutAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountData from a JSON string
about_account_data_instance = AboutAccountData.from_json(json)
# print the JSON string representation of the object
print(AboutAccountData.to_json())

# convert the object into a dict
about_account_data_dict = about_account_data_instance.to_dict()
# create an instance of AboutAccountData from a dict
about_account_data_from_dict = AboutAccountData.from_dict(about_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



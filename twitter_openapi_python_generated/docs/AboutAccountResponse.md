# AboutAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AboutAccountData**](AboutAccountData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.about_account_response import AboutAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AboutAccountResponse from a JSON string
about_account_response_instance = AboutAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AboutAccountResponse.to_json())

# convert the object into a dict
about_account_response_dict = about_account_response_instance.to_dict()
# create an instance of AboutAccountResponse from a dict
about_account_response_from_dict = AboutAccountResponse.from_dict(about_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



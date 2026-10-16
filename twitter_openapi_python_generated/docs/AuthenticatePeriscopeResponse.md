# AuthenticatePeriscopeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthenticatePeriscopeResponseData**](AuthenticatePeriscopeResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.authenticate_periscope_response import AuthenticatePeriscopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatePeriscopeResponse from a JSON string
authenticate_periscope_response_instance = AuthenticatePeriscopeResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticatePeriscopeResponse.to_json())

# convert the object into a dict
authenticate_periscope_response_dict = authenticate_periscope_response_instance.to_dict()
# create an instance of AuthenticatePeriscopeResponse from a dict
authenticate_periscope_response_from_dict = AuthenticatePeriscopeResponse.from_dict(authenticate_periscope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



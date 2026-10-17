# GrokAccountJwtResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GrokAccountJwtData**](GrokAccountJwtData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.grok_account_jwt_response import GrokAccountJwtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrokAccountJwtResponse from a JSON string
grok_account_jwt_response_instance = GrokAccountJwtResponse.from_json(json)
# print the JSON string representation of the object
print(GrokAccountJwtResponse.to_json())

# convert the object into a dict
grok_account_jwt_response_dict = grok_account_jwt_response_instance.to_dict()
# create an instance of GrokAccountJwtResponse from a dict
grok_account_jwt_response_from_dict = GrokAccountJwtResponse.from_dict(grok_account_jwt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



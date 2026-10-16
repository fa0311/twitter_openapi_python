# GrokHomeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GrokHomeResponseData**](GrokHomeResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.grok_home_response import GrokHomeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrokHomeResponse from a JSON string
grok_home_response_instance = GrokHomeResponse.from_json(json)
# print the JSON string representation of the object
print(GrokHomeResponse.to_json())

# convert the object into a dict
grok_home_response_dict = grok_home_response_instance.to_dict()
# create an instance of GrokHomeResponse from a dict
grok_home_response_from_dict = GrokHomeResponse.from_dict(grok_home_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**extensions** | [**ErrorExtensions**](ErrorExtensions.md) |  | 
**kind** | **str** |  | 
**locations** | [**List[Location]**](Location.md) |  | 
**message** | **str** |  | 
**name** | **str** |  | 
**path** | **List[object]** |  | 
**retry_after** | **int** |  | [optional] 
**source** | **str** |  | 
**tracing** | [**Tracing**](Tracing.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



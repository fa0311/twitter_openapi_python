# ErrorExtensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**kind** | **str** |  | 
**name** | **str** |  | 
**retry_after** | **int** |  | 
**source** | **str** |  | 
**tracing** | [**Tracing**](Tracing.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.error_extensions import ErrorExtensions

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorExtensions from a JSON string
error_extensions_instance = ErrorExtensions.from_json(json)
# print the JSON string representation of the object
print(ErrorExtensions.to_json())

# convert the object into a dict
error_extensions_dict = error_extensions_instance.to_dict()
# create an instance of ErrorExtensions from a dict
error_extensions_form_dict = error_extensions.from_dict(error_extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



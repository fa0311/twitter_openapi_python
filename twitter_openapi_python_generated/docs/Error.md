# Error


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**extensions** | [**ErrorExtensions**](ErrorExtensions.md) |  | 
**kind** | **str** |  | 
**locations** | [**List[Location]**](Location.md) |  | 
**message** | **str** |  | 
**name** | **str** |  | 
**path** | **List[str]** |  | 
**retry_after** | **int** |  | 
**source** | **str** |  | 
**tracing** | [**Tracing**](Tracing.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



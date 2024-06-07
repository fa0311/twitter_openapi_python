# Extensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**kind** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**tracing** | [**Tracing**](Tracing.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.extensions import Extensions

# TODO update the JSON string below
json = "{}"
# create an instance of Extensions from a JSON string
extensions_instance = Extensions.from_json(json)
# print the JSON string representation of the object
print(Extensions.to_json())

# convert the object into a dict
extensions_dict = extensions_instance.to_dict()
# create an instance of Extensions from a dict
extensions_from_dict = Extensions.from_dict(extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



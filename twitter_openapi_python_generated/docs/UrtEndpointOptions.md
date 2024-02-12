# UrtEndpointOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_params** | [**List[UrtEndpointRequestParams]**](UrtEndpointRequestParams.md) |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.urt_endpoint_options import UrtEndpointOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UrtEndpointOptions from a JSON string
urt_endpoint_options_instance = UrtEndpointOptions.from_json(json)
# print the JSON string representation of the object
print UrtEndpointOptions.to_json()

# convert the object into a dict
urt_endpoint_options_dict = urt_endpoint_options_instance.to_dict()
# create an instance of UrtEndpointOptions from a dict
urt_endpoint_options_form_dict = urt_endpoint_options.from_dict(urt_endpoint_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



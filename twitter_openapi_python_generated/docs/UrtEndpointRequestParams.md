# UrtEndpointRequestParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.urt_endpoint_request_params import UrtEndpointRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of UrtEndpointRequestParams from a JSON string
urt_endpoint_request_params_instance = UrtEndpointRequestParams.from_json(json)
# print the JSON string representation of the object
print(UrtEndpointRequestParams.to_json())

# convert the object into a dict
urt_endpoint_request_params_dict = urt_endpoint_request_params_instance.to_dict()
# create an instance of UrtEndpointRequestParams from a dict
urt_endpoint_request_params_form_dict = urt_endpoint_request_params.from_dict(urt_endpoint_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Other200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | [**Session**](Session.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.other200_response import Other200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Other200Response from a JSON string
other200_response_instance = Other200Response.from_json(json)
# print the JSON string representation of the object
print Other200Response.to_json()

# convert the object into a dict
other200_response_dict = other200_response_instance.to_dict()
# create an instance of Other200Response from a dict
other200_response_form_dict = other200_response.from_dict(other200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteListResponseData**](DeleteListResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_list_response import DeleteListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteListResponse from a JSON string
delete_list_response_instance = DeleteListResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteListResponse.to_json())

# convert the object into a dict
delete_list_response_dict = delete_list_response_instance.to_dict()
# create an instance of DeleteListResponse from a dict
delete_list_response_from_dict = DeleteListResponse.from_dict(delete_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



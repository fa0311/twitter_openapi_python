# DeleteBookmarkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteBookmarkResponseData**](DeleteBookmarkResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.delete_bookmark_response import DeleteBookmarkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBookmarkResponse from a JSON string
delete_bookmark_response_instance = DeleteBookmarkResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteBookmarkResponse.to_json())

# convert the object into a dict
delete_bookmark_response_dict = delete_bookmark_response_instance.to_dict()
# create an instance of DeleteBookmarkResponse from a dict
delete_bookmark_response_from_dict = DeleteBookmarkResponse.from_dict(delete_bookmark_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



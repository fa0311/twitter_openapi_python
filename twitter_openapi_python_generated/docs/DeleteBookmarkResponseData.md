# DeleteBookmarkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_bookmark_delete** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_bookmark_response_data import DeleteBookmarkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBookmarkResponseData from a JSON string
delete_bookmark_response_data_instance = DeleteBookmarkResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteBookmarkResponseData.to_json())

# convert the object into a dict
delete_bookmark_response_data_dict = delete_bookmark_response_data_instance.to_dict()
# create an instance of DeleteBookmarkResponseData from a dict
delete_bookmark_response_data_from_dict = DeleteBookmarkResponseData.from_dict(delete_bookmark_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



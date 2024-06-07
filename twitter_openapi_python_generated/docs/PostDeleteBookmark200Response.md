# PostDeleteBookmark200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteBookmarkResponseData**](DeleteBookmarkResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_bookmark200_response import PostDeleteBookmark200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteBookmark200Response from a JSON string
post_delete_bookmark200_response_instance = PostDeleteBookmark200Response.from_json(json)
# print the JSON string representation of the object
print(PostDeleteBookmark200Response.to_json())

# convert the object into a dict
post_delete_bookmark200_response_dict = post_delete_bookmark200_response_instance.to_dict()
# create an instance of PostDeleteBookmark200Response from a dict
post_delete_bookmark200_response_from_dict = PostDeleteBookmark200Response.from_dict(post_delete_bookmark200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



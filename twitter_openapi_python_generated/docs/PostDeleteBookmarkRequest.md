# PostDeleteBookmarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'Wlmlj2-xzyS1GN3a6cj-mQ']
**variables** | [**PostCreateBookmarkRequestVariables**](PostCreateBookmarkRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_bookmark_request import PostDeleteBookmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteBookmarkRequest from a JSON string
post_delete_bookmark_request_instance = PostDeleteBookmarkRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteBookmarkRequest.to_json())

# convert the object into a dict
post_delete_bookmark_request_dict = post_delete_bookmark_request_instance.to_dict()
# create an instance of PostDeleteBookmarkRequest from a dict
post_delete_bookmark_request_from_dict = PostDeleteBookmarkRequest.from_dict(post_delete_bookmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



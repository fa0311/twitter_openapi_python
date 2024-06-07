# PostCreateBookmarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'aoDbu3RHznuiSkQ9aNM67Q']
**variables** | [**PostCreateBookmarkRequestVariables**](PostCreateBookmarkRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_bookmark_request import PostCreateBookmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateBookmarkRequest from a JSON string
post_create_bookmark_request_instance = PostCreateBookmarkRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateBookmarkRequest.to_json())

# convert the object into a dict
post_create_bookmark_request_dict = post_create_bookmark_request_instance.to_dict()
# create an instance of PostCreateBookmarkRequest from a dict
post_create_bookmark_request_from_dict = PostCreateBookmarkRequest.from_dict(post_create_bookmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



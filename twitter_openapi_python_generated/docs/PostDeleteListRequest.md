# PostDeleteListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'UnN9Th1BDbeLjpgjGSpL3Q']
**variables** | [**PostDeleteListRequestVariables**](PostDeleteListRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_list_request import PostDeleteListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteListRequest from a JSON string
post_delete_list_request_instance = PostDeleteListRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteListRequest.to_json())

# convert the object into a dict
post_delete_list_request_dict = post_delete_list_request_instance.to_dict()
# create an instance of PostDeleteListRequest from a dict
post_delete_list_request_from_dict = PostDeleteListRequest.from_dict(post_delete_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



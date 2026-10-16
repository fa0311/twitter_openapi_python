# PostCreateListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**PostCreateListRequestFeatures**](PostCreateListRequestFeatures.md) |  | 
**query_id** | **str** |  | [default to 'zdGzorOEOslDL4XEbe2INw']
**variables** | [**PostCreateListRequestVariables**](PostCreateListRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_list_request import PostCreateListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateListRequest from a JSON string
post_create_list_request_instance = PostCreateListRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateListRequest.to_json())

# convert the object into a dict
post_create_list_request_dict = post_create_list_request_instance.to_dict()
# create an instance of PostCreateListRequest from a dict
post_create_list_request_from_dict = PostCreateListRequest.from_dict(post_create_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



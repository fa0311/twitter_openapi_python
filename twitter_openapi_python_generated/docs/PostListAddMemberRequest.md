# PostListAddMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**PostCreateListRequestFeatures**](PostCreateListRequestFeatures.md) |  | 
**query_id** | **str** |  | [default to '-Kf1YVC1rNKkPvPFk7YXZw']
**variables** | [**PostListAddMemberRequestVariables**](PostListAddMemberRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_list_add_member_request import PostListAddMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostListAddMemberRequest from a JSON string
post_list_add_member_request_instance = PostListAddMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostListAddMemberRequest.to_json())

# convert the object into a dict
post_list_add_member_request_dict = post_list_add_member_request_instance.to_dict()
# create an instance of PostListAddMemberRequest from a dict
post_list_add_member_request_from_dict = PostListAddMemberRequest.from_dict(post_list_add_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PostListRemoveMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**PostCreateListRequestFeatures**](PostCreateListRequestFeatures.md) |  | 
**query_id** | **str** |  | [default to '_2o1-wSMWGFSi5HUscn1Hw']
**variables** | [**PostListAddMemberRequestVariables**](PostListAddMemberRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_list_remove_member_request import PostListRemoveMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostListRemoveMemberRequest from a JSON string
post_list_remove_member_request_instance = PostListRemoveMemberRequest.from_json(json)
# print the JSON string representation of the object
print(PostListRemoveMemberRequest.to_json())

# convert the object into a dict
post_list_remove_member_request_dict = post_list_remove_member_request_instance.to_dict()
# create an instance of PostListRemoveMemberRequest from a dict
post_list_remove_member_request_from_dict = PostListRemoveMemberRequest.from_dict(post_list_remove_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



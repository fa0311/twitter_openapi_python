# PostListAddMemberRequestVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | [default to '1141162794290520064']
**user_id** | **str** |  | [default to '44196397']

## Example

```python
from twitter_openapi_python_generated.models.post_list_add_member_request_variables import PostListAddMemberRequestVariables

# TODO update the JSON string below
json = "{}"
# create an instance of PostListAddMemberRequestVariables from a JSON string
post_list_add_member_request_variables_instance = PostListAddMemberRequestVariables.from_json(json)
# print the JSON string representation of the object
print(PostListAddMemberRequestVariables.to_json())

# convert the object into a dict
post_list_add_member_request_variables_dict = post_list_add_member_request_variables_instance.to_dict()
# create an instance of PostListAddMemberRequestVariables from a dict
post_list_add_member_request_variables_from_dict = PostListAddMemberRequestVariables.from_dict(post_list_add_member_request_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



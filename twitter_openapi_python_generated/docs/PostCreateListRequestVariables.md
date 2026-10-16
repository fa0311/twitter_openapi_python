# PostCreateListRequestVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [default to '']
**is_private** | **bool** |  | [default to False]
**name** | **str** |  | [default to 'test']

## Example

```python
from twitter_openapi_python_generated.models.post_create_list_request_variables import PostCreateListRequestVariables

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateListRequestVariables from a JSON string
post_create_list_request_variables_instance = PostCreateListRequestVariables.from_json(json)
# print the JSON string representation of the object
print(PostCreateListRequestVariables.to_json())

# convert the object into a dict
post_create_list_request_variables_dict = post_create_list_request_variables_instance.to_dict()
# create an instance of PostCreateListRequestVariables from a dict
post_create_list_request_variables_from_dict = PostCreateListRequestVariables.from_dict(post_create_list_request_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



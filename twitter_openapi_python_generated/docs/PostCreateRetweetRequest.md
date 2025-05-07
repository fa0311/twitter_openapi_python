# PostCreateRetweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [default to 'POST']
**path** | **str** |  | [default to '/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet']
**query_id** | **str** |  | [default to 'ojPdsZsimiJrUGLR1sjUtA']
**variables** | [**PostCreateRetweetRequestVariables**](PostCreateRetweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_retweet_request import PostCreateRetweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateRetweetRequest from a JSON string
post_create_retweet_request_instance = PostCreateRetweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateRetweetRequest.to_json())

# convert the object into a dict
post_create_retweet_request_dict = post_create_retweet_request_instance.to_dict()
# create an instance of PostCreateRetweetRequest from a dict
post_create_retweet_request_from_dict = PostCreateRetweetRequest.from_dict(post_create_retweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



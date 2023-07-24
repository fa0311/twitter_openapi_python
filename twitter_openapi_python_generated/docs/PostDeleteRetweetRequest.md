# PostDeleteRetweetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'iQtK4dl5hBmXewYZuEOKVw']
**variables** | [**PostDeleteRetweetRequestVariables**](PostDeleteRetweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_retweet_request import PostDeleteRetweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteRetweetRequest from a JSON string
post_delete_retweet_request_instance = PostDeleteRetweetRequest.from_json(json)
# print the JSON string representation of the object
print PostDeleteRetweetRequest.to_json()

# convert the object into a dict
post_delete_retweet_request_dict = post_delete_retweet_request_instance.to_dict()
# create an instance of PostDeleteRetweetRequest from a dict
post_delete_retweet_request_form_dict = post_delete_retweet_request.from_dict(post_delete_retweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



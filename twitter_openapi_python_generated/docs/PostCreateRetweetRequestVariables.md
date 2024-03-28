# PostCreateRetweetRequestVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark_request** | **bool** |  | [default to False]
**tweet_id** | **str** |  | [default to '1349129669258448897']

## Example

```python
from twitter_openapi_python_generated.models.post_create_retweet_request_variables import PostCreateRetweetRequestVariables

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateRetweetRequestVariables from a JSON string
post_create_retweet_request_variables_instance = PostCreateRetweetRequestVariables.from_json(json)
# print the JSON string representation of the object
print(PostCreateRetweetRequestVariables.to_json())

# convert the object into a dict
post_create_retweet_request_variables_dict = post_create_retweet_request_variables_instance.to_dict()
# create an instance of PostCreateRetweetRequestVariables from a dict
post_create_retweet_request_variables_form_dict = post_create_retweet_request_variables.from_dict(post_create_retweet_request_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



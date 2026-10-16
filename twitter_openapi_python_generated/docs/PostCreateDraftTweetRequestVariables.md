# PostCreateDraftTweetRequestVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_tweet_request** | [**PostCreateDraftTweetRequestVariablesPostTweetRequest**](PostCreateDraftTweetRequestVariablesPostTweetRequest.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_draft_tweet_request_variables import PostCreateDraftTweetRequestVariables

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateDraftTweetRequestVariables from a JSON string
post_create_draft_tweet_request_variables_instance = PostCreateDraftTweetRequestVariables.from_json(json)
# print the JSON string representation of the object
print(PostCreateDraftTweetRequestVariables.to_json())

# convert the object into a dict
post_create_draft_tweet_request_variables_dict = post_create_draft_tweet_request_variables_instance.to_dict()
# create an instance of PostCreateDraftTweetRequestVariables from a dict
post_create_draft_tweet_request_variables_from_dict = PostCreateDraftTweetRequestVariables.from_dict(post_create_draft_tweet_request_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



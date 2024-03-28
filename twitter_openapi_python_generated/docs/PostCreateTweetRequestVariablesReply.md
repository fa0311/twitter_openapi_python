# PostCreateTweetRequestVariablesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_reply_user_ids** | **List[object]** |  | 
**in_reply_to_tweet_id** | **str** |  | [default to '1111111111111111111']

## Example

```python
from twitter_openapi_python_generated.models.post_create_tweet_request_variables_reply import PostCreateTweetRequestVariablesReply

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateTweetRequestVariablesReply from a JSON string
post_create_tweet_request_variables_reply_instance = PostCreateTweetRequestVariablesReply.from_json(json)
# print the JSON string representation of the object
print(PostCreateTweetRequestVariablesReply.to_json())

# convert the object into a dict
post_create_tweet_request_variables_reply_dict = post_create_tweet_request_variables_reply_instance.to_dict()
# create an instance of PostCreateTweetRequestVariablesReply from a dict
post_create_tweet_request_variables_reply_form_dict = post_create_tweet_request_variables_reply.from_dict(post_create_tweet_request_variables_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



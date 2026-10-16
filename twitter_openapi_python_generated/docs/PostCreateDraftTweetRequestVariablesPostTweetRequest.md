# PostCreateDraftTweetRequestVariablesPostTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_populate_reply_metadata** | **bool** |  | [default to False]
**exclude_reply_user_ids** | **List[object]** |  | 
**media_ids** | **List[object]** |  | 
**status** | **str** |  | [default to 'test']
**thread_tweets** | **List[object]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_draft_tweet_request_variables_post_tweet_request import PostCreateDraftTweetRequestVariablesPostTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateDraftTweetRequestVariablesPostTweetRequest from a JSON string
post_create_draft_tweet_request_variables_post_tweet_request_instance = PostCreateDraftTweetRequestVariablesPostTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateDraftTweetRequestVariablesPostTweetRequest.to_json())

# convert the object into a dict
post_create_draft_tweet_request_variables_post_tweet_request_dict = post_create_draft_tweet_request_variables_post_tweet_request_instance.to_dict()
# create an instance of PostCreateDraftTweetRequestVariablesPostTweetRequest from a dict
post_create_draft_tweet_request_variables_post_tweet_request_from_dict = PostCreateDraftTweetRequestVariablesPostTweetRequest.from_dict(post_create_draft_tweet_request_variables_post_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



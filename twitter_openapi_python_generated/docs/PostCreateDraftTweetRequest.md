# PostCreateDraftTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'cH9HZWz_EW9gnswvA4ZRiQ']
**variables** | [**PostCreateDraftTweetRequestVariables**](PostCreateDraftTweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_draft_tweet_request import PostCreateDraftTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateDraftTweetRequest from a JSON string
post_create_draft_tweet_request_instance = PostCreateDraftTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateDraftTweetRequest.to_json())

# convert the object into a dict
post_create_draft_tweet_request_dict = post_create_draft_tweet_request_instance.to_dict()
# create an instance of PostCreateDraftTweetRequest from a dict
post_create_draft_tweet_request_from_dict = PostCreateDraftTweetRequest.from_dict(post_create_draft_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



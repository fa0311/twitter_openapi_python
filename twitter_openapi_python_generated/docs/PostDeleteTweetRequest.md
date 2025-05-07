# PostDeleteTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [default to 'POST']
**path** | **str** |  | [default to '/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet']
**query_id** | **str** |  | [default to 'VaenaVgh5q5ih7kvyVjgtg']
**variables** | [**PostCreateRetweetRequestVariables**](PostCreateRetweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_tweet_request import PostDeleteTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteTweetRequest from a JSON string
post_delete_tweet_request_instance = PostDeleteTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteTweetRequest.to_json())

# convert the object into a dict
post_delete_tweet_request_dict = post_delete_tweet_request_instance.to_dict()
# create an instance of PostDeleteTweetRequest from a dict
post_delete_tweet_request_from_dict = PostDeleteTweetRequest.from_dict(post_delete_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



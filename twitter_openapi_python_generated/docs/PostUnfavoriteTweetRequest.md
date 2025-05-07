# PostUnfavoriteTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [default to 'POST']
**path** | **str** |  | [default to '/i/api/graphql/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet']
**query_id** | **str** |  | [default to 'ZYKSe-w7KEslx3JhSIk5LA']
**variables** | [**PostCreateRetweetRequestVariables**](PostCreateRetweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_unfavorite_tweet_request import PostUnfavoriteTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUnfavoriteTweetRequest from a JSON string
post_unfavorite_tweet_request_instance = PostUnfavoriteTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostUnfavoriteTweetRequest.to_json())

# convert the object into a dict
post_unfavorite_tweet_request_dict = post_unfavorite_tweet_request_instance.to_dict()
# create an instance of PostUnfavoriteTweetRequest from a dict
post_unfavorite_tweet_request_from_dict = PostUnfavoriteTweetRequest.from_dict(post_unfavorite_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



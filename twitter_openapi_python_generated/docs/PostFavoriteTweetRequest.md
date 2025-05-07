# PostFavoriteTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [default to 'POST']
**path** | **str** |  | [default to '/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet']
**query_id** | **str** |  | [default to 'lI07N6Otwv1PhnEgXILM7A']
**variables** | [**PostCreateBookmarkRequestVariables**](PostCreateBookmarkRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_favorite_tweet_request import PostFavoriteTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFavoriteTweetRequest from a JSON string
post_favorite_tweet_request_instance = PostFavoriteTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostFavoriteTweetRequest.to_json())

# convert the object into a dict
post_favorite_tweet_request_dict = post_favorite_tweet_request_instance.to_dict()
# create an instance of PostFavoriteTweetRequest from a dict
post_favorite_tweet_request_from_dict = PostFavoriteTweetRequest.from_dict(post_favorite_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



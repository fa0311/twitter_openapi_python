# PostCreateTweetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**PostCreateTweetRequestFeatures**](PostCreateTweetRequestFeatures.md) |  | 
**query_id** | **str** |  | [default to '8ED1SMuUGkOZVBEjiYUTfw']
**variables** | [**PostCreateTweetRequestVariables**](PostCreateTweetRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_tweet_request import PostCreateTweetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateTweetRequest from a JSON string
post_create_tweet_request_instance = PostCreateTweetRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateTweetRequest.to_json())

# convert the object into a dict
post_create_tweet_request_dict = post_create_tweet_request_instance.to_dict()
# create an instance of PostCreateTweetRequest from a dict
post_create_tweet_request_from_dict = PostCreateTweetRequest.from_dict(post_create_tweet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



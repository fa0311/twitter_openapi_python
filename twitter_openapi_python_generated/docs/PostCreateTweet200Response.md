# PostCreateTweet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTweetResponseData**](CreateTweetResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_tweet200_response import PostCreateTweet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateTweet200Response from a JSON string
post_create_tweet200_response_instance = PostCreateTweet200Response.from_json(json)
# print the JSON string representation of the object
print(PostCreateTweet200Response.to_json())

# convert the object into a dict
post_create_tweet200_response_dict = post_create_tweet200_response_instance.to_dict()
# create an instance of PostCreateTweet200Response from a dict
post_create_tweet200_response_from_dict = PostCreateTweet200Response.from_dict(post_create_tweet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



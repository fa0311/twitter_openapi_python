# PostDeleteTweet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteTweetResponseData**](DeleteTweetResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_tweet200_response import PostDeleteTweet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteTweet200Response from a JSON string
post_delete_tweet200_response_instance = PostDeleteTweet200Response.from_json(json)
# print the JSON string representation of the object
print PostDeleteTweet200Response.to_json()

# convert the object into a dict
post_delete_tweet200_response_dict = post_delete_tweet200_response_instance.to_dict()
# create an instance of PostDeleteTweet200Response from a dict
post_delete_tweet200_response_form_dict = post_delete_tweet200_response.from_dict(post_delete_tweet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PostUnfavoriteTweet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UnfavoriteTweet**](UnfavoriteTweet.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_unfavorite_tweet200_response import PostUnfavoriteTweet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostUnfavoriteTweet200Response from a JSON string
post_unfavorite_tweet200_response_instance = PostUnfavoriteTweet200Response.from_json(json)
# print the JSON string representation of the object
print PostUnfavoriteTweet200Response.to_json()

# convert the object into a dict
post_unfavorite_tweet200_response_dict = post_unfavorite_tweet200_response_instance.to_dict()
# create an instance of PostUnfavoriteTweet200Response from a dict
post_unfavorite_tweet200_response_form_dict = post_unfavorite_tweet200_response.from_dict(post_unfavorite_tweet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



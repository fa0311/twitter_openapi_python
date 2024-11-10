# UnfavoriteTweetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UnfavoriteTweet**](UnfavoriteTweet.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.unfavorite_tweet_response import UnfavoriteTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnfavoriteTweetResponse from a JSON string
unfavorite_tweet_response_instance = UnfavoriteTweetResponse.from_json(json)
# print the JSON string representation of the object
print(UnfavoriteTweetResponse.to_json())

# convert the object into a dict
unfavorite_tweet_response_dict = unfavorite_tweet_response_instance.to_dict()
# create an instance of UnfavoriteTweetResponse from a dict
unfavorite_tweet_response_from_dict = UnfavoriteTweetResponse.from_dict(unfavorite_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



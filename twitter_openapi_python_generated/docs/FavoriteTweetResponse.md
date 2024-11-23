# FavoriteTweetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FavoriteTweet**](FavoriteTweet.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.favorite_tweet_response import FavoriteTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteTweetResponse from a JSON string
favorite_tweet_response_instance = FavoriteTweetResponse.from_json(json)
# print the JSON string representation of the object
print(FavoriteTweetResponse.to_json())

# convert the object into a dict
favorite_tweet_response_dict = favorite_tweet_response_instance.to_dict()
# create an instance of FavoriteTweetResponse from a dict
favorite_tweet_response_from_dict = FavoriteTweetResponse.from_dict(favorite_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



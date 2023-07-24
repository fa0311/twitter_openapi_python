# FavoriteTweetResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FavoriteTweet**](FavoriteTweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.favorite_tweet_response_data import FavoriteTweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteTweetResponseData from a JSON string
favorite_tweet_response_data_instance = FavoriteTweetResponseData.from_json(json)
# print the JSON string representation of the object
print FavoriteTweetResponseData.to_json()

# convert the object into a dict
favorite_tweet_response_data_dict = favorite_tweet_response_data_instance.to_dict()
# create an instance of FavoriteTweetResponseData from a dict
favorite_tweet_response_data_form_dict = favorite_tweet_response_data.from_dict(favorite_tweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



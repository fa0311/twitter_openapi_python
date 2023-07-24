# UnfavoriteTweetResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UnfavoriteTweet**](UnfavoriteTweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.unfavorite_tweet_response_data import UnfavoriteTweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UnfavoriteTweetResponseData from a JSON string
unfavorite_tweet_response_data_instance = UnfavoriteTweetResponseData.from_json(json)
# print the JSON string representation of the object
print UnfavoriteTweetResponseData.to_json()

# convert the object into a dict
unfavorite_tweet_response_data_dict = unfavorite_tweet_response_data_instance.to_dict()
# create an instance of UnfavoriteTweetResponseData from a dict
unfavorite_tweet_response_data_form_dict = unfavorite_tweet_response_data.from_dict(unfavorite_tweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



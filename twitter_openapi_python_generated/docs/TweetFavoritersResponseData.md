# TweetFavoritersResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favoriters_timeline** | [**TimelineV2**](TimelineV2.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_favoriters_response_data import TweetFavoritersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetFavoritersResponseData from a JSON string
tweet_favoriters_response_data_instance = TweetFavoritersResponseData.from_json(json)
# print the JSON string representation of the object
print TweetFavoritersResponseData.to_json()

# convert the object into a dict
tweet_favoriters_response_data_dict = tweet_favoriters_response_data_instance.to_dict()
# create an instance of TweetFavoritersResponseData from a dict
tweet_favoriters_response_data_form_dict = tweet_favoriters_response_data.from_dict(tweet_favoriters_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



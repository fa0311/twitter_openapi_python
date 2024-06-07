# TweetFavoritersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetFavoritersResponseData**](TweetFavoritersResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_favoriters_response import TweetFavoritersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TweetFavoritersResponse from a JSON string
tweet_favoriters_response_instance = TweetFavoritersResponse.from_json(json)
# print the JSON string representation of the object
print(TweetFavoritersResponse.to_json())

# convert the object into a dict
tweet_favoriters_response_dict = tweet_favoriters_response_instance.to_dict()
# create an instance of TweetFavoritersResponse from a dict
tweet_favoriters_response_from_dict = TweetFavoritersResponse.from_dict(tweet_favoriters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



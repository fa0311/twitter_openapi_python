# TweetRetweetersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetRetweetersResponseData**](TweetRetweetersResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_retweeters_response import TweetRetweetersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TweetRetweetersResponse from a JSON string
tweet_retweeters_response_instance = TweetRetweetersResponse.from_json(json)
# print the JSON string representation of the object
print TweetRetweetersResponse.to_json()

# convert the object into a dict
tweet_retweeters_response_dict = tweet_retweeters_response_instance.to_dict()
# create an instance of TweetRetweetersResponse from a dict
tweet_retweeters_response_form_dict = tweet_retweeters_response.from_dict(tweet_retweeters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



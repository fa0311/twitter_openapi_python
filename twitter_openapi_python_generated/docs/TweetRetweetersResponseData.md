# TweetRetweetersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retweeters_timeline** | [**TimelineV2**](TimelineV2.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_retweeters_response_data import TweetRetweetersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetRetweetersResponseData from a JSON string
tweet_retweeters_response_data_instance = TweetRetweetersResponseData.from_json(json)
# print the JSON string representation of the object
print(TweetRetweetersResponseData.to_json())

# convert the object into a dict
tweet_retweeters_response_data_dict = tweet_retweeters_response_data_instance.to_dict()
# create an instance of TweetRetweetersResponseData from a dict
tweet_retweeters_response_data_from_dict = TweetRetweetersResponseData.from_dict(tweet_retweeters_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TweetDetailResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threaded_conversation_with_injections_v2** | [**Timeline**](Timeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_detail_response_data import TweetDetailResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDetailResponseData from a JSON string
tweet_detail_response_data_instance = TweetDetailResponseData.from_json(json)
# print the JSON string representation of the object
print(TweetDetailResponseData.to_json())

# convert the object into a dict
tweet_detail_response_data_dict = tweet_detail_response_data_instance.to_dict()
# create an instance of TweetDetailResponseData from a dict
tweet_detail_response_data_form_dict = tweet_detail_response_data.from_dict(tweet_detail_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



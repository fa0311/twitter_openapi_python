# TweetDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetDetailResponseData**](TweetDetailResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_detail_response import TweetDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TweetDetailResponse from a JSON string
tweet_detail_response_instance = TweetDetailResponse.from_json(json)
# print the JSON string representation of the object
print(TweetDetailResponse.to_json())

# convert the object into a dict
tweet_detail_response_dict = tweet_detail_response_instance.to_dict()
# create an instance of TweetDetailResponse from a dict
tweet_detail_response_form_dict = tweet_detail_response.from_dict(tweet_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



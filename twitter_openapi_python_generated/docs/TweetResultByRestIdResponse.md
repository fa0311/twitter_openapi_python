# TweetResultByRestIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetResultByRestIdData**](TweetResultByRestIdData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_result_by_rest_id_response import TweetResultByRestIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TweetResultByRestIdResponse from a JSON string
tweet_result_by_rest_id_response_instance = TweetResultByRestIdResponse.from_json(json)
# print the JSON string representation of the object
print TweetResultByRestIdResponse.to_json()

# convert the object into a dict
tweet_result_by_rest_id_response_dict = tweet_result_by_rest_id_response_instance.to_dict()
# create an instance of TweetResultByRestIdResponse from a dict
tweet_result_by_rest_id_response_form_dict = tweet_result_by_rest_id_response.from_dict(tweet_result_by_rest_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



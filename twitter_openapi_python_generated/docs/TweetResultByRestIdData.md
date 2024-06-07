# TweetResultByRestIdData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_result** | [**ItemResult**](ItemResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_result_by_rest_id_data import TweetResultByRestIdData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetResultByRestIdData from a JSON string
tweet_result_by_rest_id_data_instance = TweetResultByRestIdData.from_json(json)
# print the JSON string representation of the object
print(TweetResultByRestIdData.to_json())

# convert the object into a dict
tweet_result_by_rest_id_data_dict = tweet_result_by_rest_id_data_instance.to_dict()
# create an instance of TweetResultByRestIdData from a dict
tweet_result_by_rest_id_data_from_dict = TweetResultByRestIdData.from_dict(tweet_result_by_rest_id_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteTweetResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_retweet** | [**DeleteTweetResponseResult**](DeleteTweetResponseResult.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_tweet_response_data import DeleteTweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTweetResponseData from a JSON string
delete_tweet_response_data_instance = DeleteTweetResponseData.from_json(json)
# print the JSON string representation of the object
print DeleteTweetResponseData.to_json()

# convert the object into a dict
delete_tweet_response_data_dict = delete_tweet_response_data_instance.to_dict()
# create an instance of DeleteTweetResponseData from a dict
delete_tweet_response_data_form_dict = delete_tweet_response_data.from_dict(delete_tweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



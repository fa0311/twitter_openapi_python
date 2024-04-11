# CreateTweetResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_results** | [**CreateTweet**](CreateTweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_tweet_response_result import CreateTweetResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTweetResponseResult from a JSON string
create_tweet_response_result_instance = CreateTweetResponseResult.from_json(json)
# print the JSON string representation of the object
print(CreateTweetResponseResult.to_json())

# convert the object into a dict
create_tweet_response_result_dict = create_tweet_response_result_instance.to_dict()
# create an instance of CreateTweetResponseResult from a dict
create_tweet_response_result_form_dict = create_tweet_response_result.from_dict(create_tweet_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TweetLimitedActionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_actions** | [**List[LimitedActionResultsData]**](LimitedActionResultsData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_limited_action_results import TweetLimitedActionResults

# TODO update the JSON string below
json = "{}"
# create an instance of TweetLimitedActionResults from a JSON string
tweet_limited_action_results_instance = TweetLimitedActionResults.from_json(json)
# print the JSON string representation of the object
print(TweetLimitedActionResults.to_json())

# convert the object into a dict
tweet_limited_action_results_dict = tweet_limited_action_results_instance.to_dict()
# create an instance of TweetLimitedActionResults from a dict
tweet_limited_action_results_from_dict = TweetLimitedActionResults.from_dict(tweet_limited_action_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



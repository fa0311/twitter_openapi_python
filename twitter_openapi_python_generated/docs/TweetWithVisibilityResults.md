# TweetWithVisibilityResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**limited_action_results** | **Dict[str, object]** |  | [optional] 
**media_visibility_results** | [**MediaVisibilityResults**](MediaVisibilityResults.md) |  | [optional] 
**tweet** | [**Tweet**](Tweet.md) |  | 
**tweet_interstitial** | [**TweetInterstitial**](TweetInterstitial.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_with_visibility_results import TweetWithVisibilityResults

# TODO update the JSON string below
json = "{}"
# create an instance of TweetWithVisibilityResults from a JSON string
tweet_with_visibility_results_instance = TweetWithVisibilityResults.from_json(json)
# print the JSON string representation of the object
print(TweetWithVisibilityResults.to_json())

# convert the object into a dict
tweet_with_visibility_results_dict = tweet_with_visibility_results_instance.to_dict()
# create an instance of TweetWithVisibilityResults from a dict
tweet_with_visibility_results_from_dict = TweetWithVisibilityResults.from_dict(tweet_with_visibility_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



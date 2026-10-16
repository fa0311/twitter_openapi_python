# DraftTweetUserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DraftTweetUser**](DraftTweetUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.draft_tweet_user_results import DraftTweetUserResults

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTweetUserResults from a JSON string
draft_tweet_user_results_instance = DraftTweetUserResults.from_json(json)
# print the JSON string representation of the object
print(DraftTweetUserResults.to_json())

# convert the object into a dict
draft_tweet_user_results_dict = draft_tweet_user_results_instance.to_dict()
# create an instance of DraftTweetUserResults from a dict
draft_tweet_user_results_from_dict = DraftTweetUserResults.from_dict(draft_tweet_user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



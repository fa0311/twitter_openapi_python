# DraftTweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_id** | **str** |  | 
**tweet_create_request** | [**DraftTweetCreateRequest**](DraftTweetCreateRequest.md) |  | 
**user_results** | [**DraftTweetUserResults**](DraftTweetUserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.draft_tweet import DraftTweet

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTweet from a JSON string
draft_tweet_instance = DraftTweet.from_json(json)
# print the JSON string representation of the object
print(DraftTweet.to_json())

# convert the object into a dict
draft_tweet_dict = draft_tweet_instance.to_dict()
# create an instance of DraftTweet from a dict
draft_tweet_from_dict = DraftTweet.from_dict(draft_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



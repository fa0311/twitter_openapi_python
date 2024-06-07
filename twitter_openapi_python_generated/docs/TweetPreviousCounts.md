# TweetPreviousCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_count** | **int** |  | 
**favorite_count** | **int** |  | 
**quote_count** | **int** |  | 
**reply_count** | **int** |  | 
**retweet_count** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_previous_counts import TweetPreviousCounts

# TODO update the JSON string below
json = "{}"
# create an instance of TweetPreviousCounts from a JSON string
tweet_previous_counts_instance = TweetPreviousCounts.from_json(json)
# print the JSON string representation of the object
print(TweetPreviousCounts.to_json())

# convert the object into a dict
tweet_previous_counts_dict = tweet_previous_counts_instance.to_dict()
# create an instance of TweetPreviousCounts from a dict
tweet_previous_counts_from_dict = TweetPreviousCounts.from_dict(tweet_previous_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



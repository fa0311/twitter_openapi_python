# UserTweetCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_tweets** | **int** |  | 
**tweets** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweet_counts import UserTweetCounts

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetCounts from a JSON string
user_tweet_counts_instance = UserTweetCounts.from_json(json)
# print the JSON string representation of the object
print(UserTweetCounts.to_json())

# convert the object into a dict
user_tweet_counts_dict = user_tweet_counts_instance.to_dict()
# create an instance of UserTweetCounts from a dict
user_tweet_counts_from_dict = UserTweetCounts.from_dict(user_tweet_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TweetPreviewDisplayTweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_count** | **int** |  | 
**core** | [**UserResultCore**](UserResultCore.md) |  | 
**created_at** | **str** |  | 
**entities** | **object** |  | 
**favorite_count** | **int** |  | 
**quote_count** | **int** |  | 
**reply_count** | **int** |  | 
**rest_id** | **str** |  | 
**retweet_count** | **int** |  | 
**text** | **str** |  | 
**view_count** | [**TweetPreviewDisplayTweetViewCount**](TweetPreviewDisplayTweetViewCount.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_preview_display_tweet import TweetPreviewDisplayTweet

# TODO update the JSON string below
json = "{}"
# create an instance of TweetPreviewDisplayTweet from a JSON string
tweet_preview_display_tweet_instance = TweetPreviewDisplayTweet.from_json(json)
# print the JSON string representation of the object
print(TweetPreviewDisplayTweet.to_json())

# convert the object into a dict
tweet_preview_display_tweet_dict = tweet_preview_display_tweet_instance.to_dict()
# create an instance of TweetPreviewDisplayTweet from a dict
tweet_preview_display_tweet_from_dict = TweetPreviewDisplayTweet.from_dict(tweet_preview_display_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



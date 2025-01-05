# TweetPreviewDisplay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**cta** | [**TweetPreviewDisplayCta**](TweetPreviewDisplayCta.md) |  | 
**limited_action_results** | [**TweetLimitedActionResults**](TweetLimitedActionResults.md) |  | 
**tweet** | [**TweetPreviewDisplayTweet**](TweetPreviewDisplayTweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_preview_display import TweetPreviewDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of TweetPreviewDisplay from a JSON string
tweet_preview_display_instance = TweetPreviewDisplay.from_json(json)
# print the JSON string representation of the object
print(TweetPreviewDisplay.to_json())

# convert the object into a dict
tweet_preview_display_dict = tweet_preview_display_instance.to_dict()
# create an instance of TweetPreviewDisplay from a dict
tweet_preview_display_from_dict = TweetPreviewDisplay.from_dict(tweet_preview_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



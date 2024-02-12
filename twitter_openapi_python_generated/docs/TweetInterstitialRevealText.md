# TweetInterstitialRevealText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[TweetInterstitialTextEntity]**](TweetInterstitialTextEntity.md) |  | 
**rtl** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_interstitial_reveal_text import TweetInterstitialRevealText

# TODO update the JSON string below
json = "{}"
# create an instance of TweetInterstitialRevealText from a JSON string
tweet_interstitial_reveal_text_instance = TweetInterstitialRevealText.from_json(json)
# print the JSON string representation of the object
print TweetInterstitialRevealText.to_json()

# convert the object into a dict
tweet_interstitial_reveal_text_dict = tweet_interstitial_reveal_text_instance.to_dict()
# create an instance of TweetInterstitialRevealText from a dict
tweet_interstitial_reveal_text_form_dict = tweet_interstitial_reveal_text.from_dict(tweet_interstitial_reveal_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



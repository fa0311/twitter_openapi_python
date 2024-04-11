# TweetInterstitialText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[TweetInterstitialTextEntity]**](TweetInterstitialTextEntity.md) |  | 
**rtl** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_interstitial_text import TweetInterstitialText

# TODO update the JSON string below
json = "{}"
# create an instance of TweetInterstitialText from a JSON string
tweet_interstitial_text_instance = TweetInterstitialText.from_json(json)
# print the JSON string representation of the object
print(TweetInterstitialText.to_json())

# convert the object into a dict
tweet_interstitial_text_dict = tweet_interstitial_text_instance.to_dict()
# create an instance of TweetInterstitialText from a dict
tweet_interstitial_text_form_dict = tweet_interstitial_text.from_dict(tweet_interstitial_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



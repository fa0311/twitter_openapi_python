# TweetInterstitial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**display_type** | **str** |  | 
**reveal_text** | [**TweetInterstitialRevealText**](TweetInterstitialRevealText.md) |  | 
**text** | [**TweetInterstitialText**](TweetInterstitialText.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_interstitial import TweetInterstitial

# TODO update the JSON string below
json = "{}"
# create an instance of TweetInterstitial from a JSON string
tweet_interstitial_instance = TweetInterstitial.from_json(json)
# print the JSON string representation of the object
print TweetInterstitial.to_json()

# convert the object into a dict
tweet_interstitial_dict = tweet_interstitial_instance.to_dict()
# create an instance of TweetInterstitial from a dict
tweet_interstitial_form_dict = tweet_interstitial.from_dict(tweet_interstitial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TweetInterstitialTextEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** |  | 
**url_type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_interstitial_text_entity_ref import TweetInterstitialTextEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of TweetInterstitialTextEntityRef from a JSON string
tweet_interstitial_text_entity_ref_instance = TweetInterstitialTextEntityRef.from_json(json)
# print the JSON string representation of the object
print(TweetInterstitialTextEntityRef.to_json())

# convert the object into a dict
tweet_interstitial_text_entity_ref_dict = tweet_interstitial_text_entity_ref_instance.to_dict()
# create an instance of TweetInterstitialTextEntityRef from a dict
tweet_interstitial_text_entity_ref_from_dict = TweetInterstitialTextEntityRef.from_dict(tweet_interstitial_text_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



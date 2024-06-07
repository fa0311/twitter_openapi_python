# TweetInterstitialTextEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**TweetInterstitialTextEntityRef**](TweetInterstitialTextEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_interstitial_text_entity import TweetInterstitialTextEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TweetInterstitialTextEntity from a JSON string
tweet_interstitial_text_entity_instance = TweetInterstitialTextEntity.from_json(json)
# print the JSON string representation of the object
print(TweetInterstitialTextEntity.to_json())

# convert the object into a dict
tweet_interstitial_text_entity_dict = tweet_interstitial_text_entity_instance.to_dict()
# create an instance of TweetInterstitialTextEntity from a dict
tweet_interstitial_text_entity_from_dict = TweetInterstitialTextEntity.from_dict(tweet_interstitial_text_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



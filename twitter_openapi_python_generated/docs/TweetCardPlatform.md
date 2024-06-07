# TweetCardPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | [**TweetCardPlatformAudience**](TweetCardPlatformAudience.md) |  | 
**device** | [**TweetCardPlatformDevice**](TweetCardPlatformDevice.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_card_platform import TweetCardPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of TweetCardPlatform from a JSON string
tweet_card_platform_instance = TweetCardPlatform.from_json(json)
# print the JSON string representation of the object
print(TweetCardPlatform.to_json())

# convert the object into a dict
tweet_card_platform_dict = tweet_card_platform_instance.to_dict()
# create an instance of TweetCardPlatform from a dict
tweet_card_platform_from_dict = TweetCardPlatform.from_dict(tweet_card_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



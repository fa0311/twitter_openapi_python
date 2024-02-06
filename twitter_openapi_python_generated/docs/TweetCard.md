# TweetCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy** | [**TweetCardLegacy**](TweetCardLegacy.md) |  | [optional] 
**rest_id** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_card import TweetCard

# TODO update the JSON string below
json = "{}"
# create an instance of TweetCard from a JSON string
tweet_card_instance = TweetCard.from_json(json)
# print the JSON string representation of the object
print TweetCard.to_json()

# convert the object into a dict
tweet_card_dict = tweet_card_instance.to_dict()
# create an instance of TweetCard from a dict
tweet_card_form_dict = tweet_card.from_dict(tweet_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



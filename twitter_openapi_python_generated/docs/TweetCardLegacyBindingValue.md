# TweetCardLegacyBindingValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | [**TweetCardLegacyBindingValueData**](TweetCardLegacyBindingValueData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_card_legacy_binding_value import TweetCardLegacyBindingValue

# TODO update the JSON string below
json = "{}"
# create an instance of TweetCardLegacyBindingValue from a JSON string
tweet_card_legacy_binding_value_instance = TweetCardLegacyBindingValue.from_json(json)
# print the JSON string representation of the object
print TweetCardLegacyBindingValue.to_json()

# convert the object into a dict
tweet_card_legacy_binding_value_dict = tweet_card_legacy_binding_value_instance.to_dict()
# create an instance of TweetCardLegacyBindingValue from a dict
tweet_card_legacy_binding_value_form_dict = tweet_card_legacy_binding_value.from_dict(tweet_card_legacy_binding_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



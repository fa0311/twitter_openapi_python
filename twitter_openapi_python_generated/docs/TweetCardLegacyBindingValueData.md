# TweetCardLegacyBindingValueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean_value** | **bool** |  | [optional] 
**scribe_key** | **str** |  | [optional] 
**string_value** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_card_legacy_binding_value_data import TweetCardLegacyBindingValueData

# TODO update the JSON string below
json = "{}"
# create an instance of TweetCardLegacyBindingValueData from a JSON string
tweet_card_legacy_binding_value_data_instance = TweetCardLegacyBindingValueData.from_json(json)
# print the JSON string representation of the object
print TweetCardLegacyBindingValueData.to_json()

# convert the object into a dict
tweet_card_legacy_binding_value_data_dict = tweet_card_legacy_binding_value_data_instance.to_dict()
# create an instance of TweetCardLegacyBindingValueData from a dict
tweet_card_legacy_binding_value_data_form_dict = tweet_card_legacy_binding_value_data.from_dict(tweet_card_legacy_binding_value_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



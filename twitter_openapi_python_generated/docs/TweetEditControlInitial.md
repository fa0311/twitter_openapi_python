# TweetEditControlInitial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_tweet_ids** | **List[str]** |  | 
**editable_until_msecs** | **str** |  | 
**edits_remaining** | **str** |  | 
**is_edit_eligible** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_edit_control_initial import TweetEditControlInitial

# TODO update the JSON string below
json = "{}"
# create an instance of TweetEditControlInitial from a JSON string
tweet_edit_control_initial_instance = TweetEditControlInitial.from_json(json)
# print the JSON string representation of the object
print(TweetEditControlInitial.to_json())

# convert the object into a dict
tweet_edit_control_initial_dict = tweet_edit_control_initial_instance.to_dict()
# create an instance of TweetEditControlInitial from a dict
tweet_edit_control_initial_form_dict = tweet_edit_control_initial.from_dict(tweet_edit_control_initial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



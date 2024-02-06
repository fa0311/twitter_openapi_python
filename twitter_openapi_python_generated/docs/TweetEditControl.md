# TweetEditControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_control_initial** | [**TweetEditControlInitial**](TweetEditControlInitial.md) |  | [optional] 
**edit_tweet_ids** | **List[str]** |  | [optional] 
**editable_until_msecs** | **str** |  | [optional] 
**edits_remaining** | **str** |  | [optional] 
**initial_tweet_id** | **str** |  | [optional] 
**is_edit_eligible** | **bool** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet_edit_control import TweetEditControl

# TODO update the JSON string below
json = "{}"
# create an instance of TweetEditControl from a JSON string
tweet_edit_control_instance = TweetEditControl.from_json(json)
# print the JSON string representation of the object
print TweetEditControl.to_json()

# convert the object into a dict
tweet_edit_control_dict = tweet_edit_control_instance.to_dict()
# create an instance of TweetEditControl from a dict
tweet_edit_control_form_dict = tweet_edit_control.from_dict(tweet_edit_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



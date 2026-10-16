# FeedbackActionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | [**FeedbackAction**](FeedbackAction.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.feedback_action_entry import FeedbackActionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackActionEntry from a JSON string
feedback_action_entry_instance = FeedbackActionEntry.from_json(json)
# print the JSON string representation of the object
print(FeedbackActionEntry.to_json())

# convert the object into a dict
feedback_action_entry_dict = feedback_action_entry_instance.to_dict()
# create an instance of FeedbackActionEntry from a dict
feedback_action_entry_from_dict = FeedbackActionEntry.from_dict(feedback_action_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



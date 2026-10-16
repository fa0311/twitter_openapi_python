# FeedbackAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_keys** | **List[str]** |  | [optional] 
**client_event_info** | [**FeedbackClientEventInfo**](FeedbackClientEventInfo.md) |  | [optional] 
**confirmation** | **str** |  | 
**confirmation_display_type** | **str** |  | [optional] 
**feedback_type** | **str** |  | 
**feedback_url** | **str** |  | [optional] 
**has_undo_action** | **bool** |  | 
**icon** | **str** |  | [optional] 
**prompt** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.feedback_action import FeedbackAction

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackAction from a JSON string
feedback_action_instance = FeedbackAction.from_json(json)
# print the JSON string representation of the object
print(FeedbackAction.to_json())

# convert the object into a dict
feedback_action_dict = feedback_action_instance.to_dict()
# create an instance of FeedbackAction from a dict
feedback_action_from_dict = FeedbackAction.from_dict(feedback_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



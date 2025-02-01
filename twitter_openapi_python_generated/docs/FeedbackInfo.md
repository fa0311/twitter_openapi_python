# FeedbackInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | [optional] 
**feedback_keys** | **List[str]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.feedback_info import FeedbackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackInfo from a JSON string
feedback_info_instance = FeedbackInfo.from_json(json)
# print the JSON string representation of the object
print(FeedbackInfo.to_json())

# convert the object into a dict
feedback_info_dict = feedback_info_instance.to_dict()
# create an instance of FeedbackInfo from a dict
feedback_info_from_dict = FeedbackInfo.from_dict(feedback_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



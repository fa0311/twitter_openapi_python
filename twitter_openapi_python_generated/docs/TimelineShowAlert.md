# TimelineShowAlert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | **str** |  | [optional] 
**color_config** | **Dict[str, object]** |  | [optional] 
**display_duration_ms** | **int** |  | [optional] 
**display_location** | **str** |  | [optional] 
**icon_display_info** | **Dict[str, object]** |  | [optional] 
**rich_text** | [**TimelineShowAlertRichText**](TimelineShowAlertRichText.md) |  | 
**trigger_delay_ms** | **int** |  | [optional] 
**type** | [**InstructionType**](InstructionType.md) |  | 
**users_results** | [**List[UserResults]**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_show_alert import TimelineShowAlert

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineShowAlert from a JSON string
timeline_show_alert_instance = TimelineShowAlert.from_json(json)
# print the JSON string representation of the object
print TimelineShowAlert.to_json()

# convert the object into a dict
timeline_show_alert_dict = timeline_show_alert_instance.to_dict()
# create an instance of TimelineShowAlert from a dict
timeline_show_alert_form_dict = timeline_show_alert.from_dict(timeline_show_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



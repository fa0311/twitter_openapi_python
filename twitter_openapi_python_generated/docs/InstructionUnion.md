# InstructionUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TimelineAddEntry]**](TimelineAddEntry.md) |  | 
**type** | [**InstructionType**](InstructionType.md) |  | 
**module_entry_id** | **str** |  | 
**module_items** | [**List[ModuleItem]**](ModuleItem.md) |  | 
**prepend** | **bool** |  | [optional] 
**entry** | [**TimelineAddEntry**](TimelineAddEntry.md) |  | 
**entry_id_to_replace** | **str** |  | 
**alert_type** | **str** |  | 
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | 
**color_config** | [**TimelineShowAlertColorConfig**](TimelineShowAlertColorConfig.md) |  | 
**display_duration_ms** | **int** |  | 
**display_location** | **str** |  | 
**icon_display_info** | [**TimelineShowAlertIconDisplayInfo**](TimelineShowAlertIconDisplayInfo.md) |  | 
**rich_text** | [**TimelineShowAlertRichText**](TimelineShowAlertRichText.md) |  | 
**trigger_delay_ms** | **int** |  | 
**users_results** | [**List[UserResults]**](UserResults.md) |  | [optional] 
**direction** | **str** |  | 
**cover** | [**TimelineHalfCover**](TimelineHalfCover.md) |  | 
**sort_index** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.instruction_union import InstructionUnion

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionUnion from a JSON string
instruction_union_instance = InstructionUnion.from_json(json)
# print the JSON string representation of the object
print(InstructionUnion.to_json())

# convert the object into a dict
instruction_union_dict = instruction_union_instance.to_dict()
# create an instance of InstructionUnion from a dict
instruction_union_from_dict = InstructionUnion.from_dict(instruction_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



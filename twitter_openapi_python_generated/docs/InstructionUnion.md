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
**alert_type** | **str** |  | [optional] 
**color_config** | **Dict[str, object]** |  | [optional] 
**display_duration_ms** | **int** |  | [optional] 
**display_location** | **str** |  | [optional] 
**icon_display_info** | **Dict[str, object]** |  | [optional] 
**rich_text** | [**TimelineShowAlertRichText**](TimelineShowAlertRichText.md) |  | 
**trigger_delay_ms** | **int** |  | [optional] 
**users_results** | [**List[UserResults]**](UserResults.md) |  | 
**direction** | **str** |  | 
**client_event_info** | [**ClientEventInfo**](ClientEventInfo.md) |  | 
**cover** | [**TimelineHalfCover**](TimelineHalfCover.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.instruction_union import InstructionUnion

# TODO update the JSON string below
json = "{}"
# create an instance of InstructionUnion from a JSON string
instruction_union_instance = InstructionUnion.from_json(json)
# print the JSON string representation of the object
print InstructionUnion.to_json()

# convert the object into a dict
instruction_union_dict = instruction_union_instance.to_dict()
# create an instance of InstructionUnion from a dict
instruction_union_form_dict = instruction_union.from_dict(instruction_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimelineAddToModule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_entry_id** | **str** |  | 
**module_items** | [**List[ModuleItem]**](ModuleItem.md) |  | 
**prepend** | **bool** |  | [optional] 
**type** | [**InstructionType**](InstructionType.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_add_to_module import TimelineAddToModule

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineAddToModule from a JSON string
timeline_add_to_module_instance = TimelineAddToModule.from_json(json)
# print the JSON string representation of the object
print TimelineAddToModule.to_json()

# convert the object into a dict
timeline_add_to_module_dict = timeline_add_to_module_instance.to_dict()
# create an instance of TimelineAddToModule from a dict
timeline_add_to_module_form_dict = timeline_add_to_module.from_dict(timeline_add_to_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



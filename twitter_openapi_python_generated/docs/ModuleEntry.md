# ModuleEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_event_info** | **object** |  | 
**item_content** | [**ItemContentUnion**](ItemContentUnion.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.module_entry import ModuleEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleEntry from a JSON string
module_entry_instance = ModuleEntry.from_json(json)
# print the JSON string representation of the object
print ModuleEntry.to_json()

# convert the object into a dict
module_entry_dict = module_entry_instance.to_dict()
# create an instance of ModuleEntry from a dict
module_entry_form_dict = module_entry.from_dict(module_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



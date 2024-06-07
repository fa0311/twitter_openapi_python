# ModuleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **str** |  | 
**item** | [**ModuleEntry**](ModuleEntry.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.module_item import ModuleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleItem from a JSON string
module_item_instance = ModuleItem.from_json(json)
# print the JSON string representation of the object
print(ModuleItem.to_json())

# convert the object into a dict
module_item_dict = module_item_instance.to_dict()
# create an instance of ModuleItem from a dict
module_item_from_dict = ModuleItem.from_dict(module_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



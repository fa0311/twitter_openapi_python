# ModuleHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_type** | **str** |  | 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**sticky** | **bool** |  | [optional] 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.module_header import ModuleHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleHeader from a JSON string
module_header_instance = ModuleHeader.from_json(json)
# print the JSON string representation of the object
print(ModuleHeader.to_json())

# convert the object into a dict
module_header_dict = module_header_instance.to_dict()
# create an instance of ModuleHeader from a dict
module_header_from_dict = ModuleHeader.from_dict(module_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



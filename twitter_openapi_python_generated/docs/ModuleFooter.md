# ModuleFooter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_type** | **str** |  | 
**landing_url** | [**LandingUrl**](LandingUrl.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.module_footer import ModuleFooter

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleFooter from a JSON string
module_footer_instance = ModuleFooter.from_json(json)
# print the JSON string representation of the object
print(ModuleFooter.to_json())

# convert the object into a dict
module_footer_dict = module_footer_instance.to_dict()
# create an instance of ModuleFooter from a dict
module_footer_from_dict = ModuleFooter.from_dict(module_footer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



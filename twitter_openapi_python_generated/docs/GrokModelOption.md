# GrokModelOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**icon_name** | **str** |  | 
**id** | **str** |  | 
**is_analyze_enabled** | **bool** |  | 
**is_enabled** | **bool** |  | 
**is_enhance_enabled** | **bool** |  | 
**mode** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_model_option import GrokModelOption

# TODO update the JSON string below
json = "{}"
# create an instance of GrokModelOption from a JSON string
grok_model_option_instance = GrokModelOption.from_json(json)
# print the JSON string representation of the object
print(GrokModelOption.to_json())

# convert the object into a dict
grok_model_option_dict = grok_model_option_instance.to_dict()
# create an instance of GrokModelOption from a dict
grok_model_option_from_dict = GrokModelOption.from_dict(grok_model_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



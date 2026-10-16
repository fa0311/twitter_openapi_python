# GrokHome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_grok_mode** | **str** |  | 
**default_grok_model_option_id** | **str** |  | 
**eligible_for_grok** | **bool** |  | 
**free_access_enabled** | **bool** |  | 
**grok_model_options** | [**List[GrokModelOption]**](GrokModelOption.md) |  | 
**grok_version** | **str** |  | 
**ineligible_reasons** | **List[object]** |  | 
**layout** | [**GrokHomeLayout**](GrokHomeLayout.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_home import GrokHome

# TODO update the JSON string below
json = "{}"
# create an instance of GrokHome from a JSON string
grok_home_instance = GrokHome.from_json(json)
# print the JSON string representation of the object
print(GrokHome.to_json())

# convert the object into a dict
grok_home_dict = grok_home_instance.to_dict()
# create an instance of GrokHome from a dict
grok_home_from_dict = GrokHome.from_dict(grok_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GrokHomeLayoutSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompts** | [**List[GrokHomePrompt]**](GrokHomePrompt.md) |  | 
**section_type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_home_layout_section import GrokHomeLayoutSection

# TODO update the JSON string below
json = "{}"
# create an instance of GrokHomeLayoutSection from a JSON string
grok_home_layout_section_instance = GrokHomeLayoutSection.from_json(json)
# print the JSON string representation of the object
print(GrokHomeLayoutSection.to_json())

# convert the object into a dict
grok_home_layout_section_dict = grok_home_layout_section_instance.to_dict()
# create an instance of GrokHomeLayoutSection from a dict
grok_home_layout_section_from_dict = GrokHomeLayoutSection.from_dict(grok_home_layout_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GrokHomeLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**sections** | [**List[GrokHomeLayoutSection]**](GrokHomeLayoutSection.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_home_layout import GrokHomeLayout

# TODO update the JSON string below
json = "{}"
# create an instance of GrokHomeLayout from a JSON string
grok_home_layout_instance = GrokHomeLayout.from_json(json)
# print the JSON string representation of the object
print(GrokHomeLayout.to_json())

# convert the object into a dict
grok_home_layout_dict = grok_home_layout_instance.to_dict()
# create an instance of GrokHomeLayout from a dict
grok_home_layout_from_dict = GrokHomeLayout.from_dict(grok_home_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



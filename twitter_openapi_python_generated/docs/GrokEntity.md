# GrokEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **str** |  | 
**ref** | [**GrokEntityRef**](GrokEntityRef.md) |  | 
**to_index** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_entity import GrokEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GrokEntity from a JSON string
grok_entity_instance = GrokEntity.from_json(json)
# print the JSON string representation of the object
print(GrokEntity.to_json())

# convert the object into a dict
grok_entity_dict = grok_entity_instance.to_dict()
# create an instance of GrokEntity from a dict
grok_entity_from_dict = GrokEntity.from_dict(grok_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



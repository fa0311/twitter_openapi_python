# GrokEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_url** | **str** |  | [optional] 
**expanded_url** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | [optional] 
**url_type** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.grok_entity_ref import GrokEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of GrokEntityRef from a JSON string
grok_entity_ref_instance = GrokEntityRef.from_json(json)
# print the JSON string representation of the object
print(GrokEntityRef.to_json())

# convert the object into a dict
grok_entity_ref_dict = grok_entity_ref_instance.to_dict()
# create an instance of GrokEntityRef from a dict
grok_entity_ref_from_dict = GrokEntityRef.from_dict(grok_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



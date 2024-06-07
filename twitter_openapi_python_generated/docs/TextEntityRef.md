# TextEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** |  | 
**url_type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.text_entity_ref import TextEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of TextEntityRef from a JSON string
text_entity_ref_instance = TextEntityRef.from_json(json)
# print the JSON string representation of the object
print(TextEntityRef.to_json())

# convert the object into a dict
text_entity_ref_dict = text_entity_ref_instance.to_dict()
# create an instance of TextEntityRef from a dict
text_entity_ref_from_dict = TextEntityRef.from_dict(text_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



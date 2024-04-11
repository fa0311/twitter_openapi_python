# TextEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**TextEntityRef**](TextEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.text_entity import TextEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TextEntity from a JSON string
text_entity_instance = TextEntity.from_json(json)
# print the JSON string representation of the object
print(TextEntity.to_json())

# convert the object into a dict
text_entity_dict = text_entity_instance.to_dict()
# create an instance of TextEntity from a dict
text_entity_form_dict = text_entity.from_dict(text_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



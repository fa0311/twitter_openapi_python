# ExtendedEntities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**List[MediaExtended]**](MediaExtended.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.extended_entities import ExtendedEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedEntities from a JSON string
extended_entities_instance = ExtendedEntities.from_json(json)
# print the JSON string representation of the object
print ExtendedEntities.to_json()

# convert the object into a dict
extended_entities_dict = extended_entities_instance.to_dict()
# create an instance of ExtendedEntities from a dict
extended_entities_form_dict = extended_entities.from_dict(extended_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



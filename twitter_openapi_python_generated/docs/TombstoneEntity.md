# TombstoneEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | [optional] 
**ref** | [**TombstoneRef**](TombstoneRef.md) |  | [optional] 
**to_index** | **int** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tombstone_entity import TombstoneEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TombstoneEntity from a JSON string
tombstone_entity_instance = TombstoneEntity.from_json(json)
# print the JSON string representation of the object
print(TombstoneEntity.to_json())

# convert the object into a dict
tombstone_entity_dict = tombstone_entity_instance.to_dict()
# create an instance of TombstoneEntity from a dict
tombstone_entity_from_dict = TombstoneEntity.from_dict(tombstone_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



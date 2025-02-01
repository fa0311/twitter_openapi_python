# TombstoneRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_type** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tombstone_ref import TombstoneRef

# TODO update the JSON string below
json = "{}"
# create an instance of TombstoneRef from a JSON string
tombstone_ref_instance = TombstoneRef.from_json(json)
# print the JSON string representation of the object
print(TombstoneRef.to_json())

# convert the object into a dict
tombstone_ref_dict = tombstone_ref_instance.to_dict()
# create an instance of TombstoneRef from a dict
tombstone_ref_from_dict = TombstoneRef.from_dict(tombstone_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



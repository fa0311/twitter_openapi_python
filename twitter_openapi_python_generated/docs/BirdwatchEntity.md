# BirdwatchEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**BirdwatchEntityRef**](BirdwatchEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_entity import BirdwatchEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchEntity from a JSON string
birdwatch_entity_instance = BirdwatchEntity.from_json(json)
# print the JSON string representation of the object
print BirdwatchEntity.to_json()

# convert the object into a dict
birdwatch_entity_dict = birdwatch_entity_instance.to_dict()
# create an instance of BirdwatchEntity from a dict
birdwatch_entity_form_dict = birdwatch_entity.from_dict(birdwatch_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



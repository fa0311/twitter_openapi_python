# BirdwatchEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | [optional] 
**url_type** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_entity_ref import BirdwatchEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchEntityRef from a JSON string
birdwatch_entity_ref_instance = BirdwatchEntityRef.from_json(json)
# print the JSON string representation of the object
print(BirdwatchEntityRef.to_json())

# convert the object into a dict
birdwatch_entity_ref_dict = birdwatch_entity_ref_instance.to_dict()
# create an instance of BirdwatchEntityRef from a dict
birdwatch_entity_ref_form_dict = birdwatch_entity_ref.from_dict(birdwatch_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



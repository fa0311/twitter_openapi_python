# Timeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | [**List[InstructionUnion]**](InstructionUnion.md) |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**response_objects** | **Dict[str, object]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline import Timeline

# TODO update the JSON string below
json = "{}"
# create an instance of Timeline from a JSON string
timeline_instance = Timeline.from_json(json)
# print the JSON string representation of the object
print Timeline.to_json()

# convert the object into a dict
timeline_dict = timeline_instance.to_dict()
# create an instance of Timeline from a dict
timeline_form_dict = timeline.from_dict(timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



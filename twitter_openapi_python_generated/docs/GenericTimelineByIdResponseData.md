# GenericTimelineByIdResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.generic_timeline_by_id_response_data import GenericTimelineByIdResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GenericTimelineByIdResponseData from a JSON string
generic_timeline_by_id_response_data_instance = GenericTimelineByIdResponseData.from_json(json)
# print the JSON string representation of the object
print(GenericTimelineByIdResponseData.to_json())

# convert the object into a dict
generic_timeline_by_id_response_data_dict = generic_timeline_by_id_response_data_instance.to_dict()
# create an instance of GenericTimelineByIdResponseData from a dict
generic_timeline_by_id_response_data_from_dict = GenericTimelineByIdResponseData.from_dict(generic_timeline_by_id_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



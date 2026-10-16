# GenericTimelineByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GenericTimelineByIdResponseData**](GenericTimelineByIdResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.generic_timeline_by_id_response import GenericTimelineByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericTimelineByIdResponse from a JSON string
generic_timeline_by_id_response_instance = GenericTimelineByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GenericTimelineByIdResponse.to_json())

# convert the object into a dict
generic_timeline_by_id_response_dict = generic_timeline_by_id_response_instance.to_dict()
# create an instance of GenericTimelineByIdResponse from a dict
generic_timeline_by_id_response_from_dict = GenericTimelineByIdResponse.from_dict(generic_timeline_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



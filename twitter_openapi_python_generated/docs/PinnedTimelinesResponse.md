# PinnedTimelinesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PinnedTimelinesResponseData**](PinnedTimelinesResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.pinned_timelines_response import PinnedTimelinesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedTimelinesResponse from a JSON string
pinned_timelines_response_instance = PinnedTimelinesResponse.from_json(json)
# print the JSON string representation of the object
print(PinnedTimelinesResponse.to_json())

# convert the object into a dict
pinned_timelines_response_dict = pinned_timelines_response_instance.to_dict()
# create an instance of PinnedTimelinesResponse from a dict
pinned_timelines_response_from_dict = PinnedTimelinesResponse.from_dict(pinned_timelines_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



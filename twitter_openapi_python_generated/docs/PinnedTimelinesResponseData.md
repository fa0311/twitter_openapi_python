# PinnedTimelinesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pinned_timelines** | [**PinnedTimelines**](PinnedTimelines.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.pinned_timelines_response_data import PinnedTimelinesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedTimelinesResponseData from a JSON string
pinned_timelines_response_data_instance = PinnedTimelinesResponseData.from_json(json)
# print the JSON string representation of the object
print(PinnedTimelinesResponseData.to_json())

# convert the object into a dict
pinned_timelines_response_data_dict = pinned_timelines_response_data_instance.to_dict()
# create an instance of PinnedTimelinesResponseData from a dict
pinned_timelines_response_data_from_dict = PinnedTimelinesResponseData.from_dict(pinned_timelines_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



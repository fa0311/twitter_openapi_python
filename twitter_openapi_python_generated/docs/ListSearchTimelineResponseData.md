# ListSearchTimelineResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_by_raw_query** | [**ListSearch**](ListSearch.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_search_timeline_response_data import ListSearchTimelineResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListSearchTimelineResponseData from a JSON string
list_search_timeline_response_data_instance = ListSearchTimelineResponseData.from_json(json)
# print the JSON string representation of the object
print(ListSearchTimelineResponseData.to_json())

# convert the object into a dict
list_search_timeline_response_data_dict = list_search_timeline_response_data_instance.to_dict()
# create an instance of ListSearchTimelineResponseData from a dict
list_search_timeline_response_data_from_dict = ListSearchTimelineResponseData.from_dict(list_search_timeline_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



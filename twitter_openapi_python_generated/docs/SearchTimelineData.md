# SearchTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_by_raw_query** | [**SearchByRawQuery**](SearchByRawQuery.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.search_timeline_data import SearchTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTimelineData from a JSON string
search_timeline_data_instance = SearchTimelineData.from_json(json)
# print the JSON string representation of the object
print(SearchTimelineData.to_json())

# convert the object into a dict
search_timeline_data_dict = search_timeline_data_instance.to_dict()
# create an instance of SearchTimelineData from a dict
search_timeline_data_form_dict = search_timeline_data.from_dict(search_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



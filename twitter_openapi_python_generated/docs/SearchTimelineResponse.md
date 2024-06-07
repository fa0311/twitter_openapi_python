# SearchTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SearchTimelineData**](SearchTimelineData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.search_timeline_response import SearchTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTimelineResponse from a JSON string
search_timeline_response_instance = SearchTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(SearchTimelineResponse.to_json())

# convert the object into a dict
search_timeline_response_dict = search_timeline_response_instance.to_dict()
# create an instance of SearchTimelineResponse from a dict
search_timeline_response_from_dict = SearchTimelineResponse.from_dict(search_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



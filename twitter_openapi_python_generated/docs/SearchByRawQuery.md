# SearchByRawQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_timeline** | [**SearchTimeline**](SearchTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.search_by_raw_query import SearchByRawQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchByRawQuery from a JSON string
search_by_raw_query_instance = SearchByRawQuery.from_json(json)
# print the JSON string representation of the object
print SearchByRawQuery.to_json()

# convert the object into a dict
search_by_raw_query_dict = search_by_raw_query_instance.to_dict()
# create an instance of SearchByRawQuery from a dict
search_by_raw_query_form_dict = search_by_raw_query.from_dict(search_by_raw_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



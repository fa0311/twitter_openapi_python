# SearchTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**Timeline**](Timeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.search_timeline import SearchTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTimeline from a JSON string
search_timeline_instance = SearchTimeline.from_json(json)
# print the JSON string representation of the object
print SearchTimeline.to_json()

# convert the object into a dict
search_timeline_dict = search_timeline_instance.to_dict()
# create an instance of SearchTimeline from a dict
search_timeline_form_dict = search_timeline.from_dict(search_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



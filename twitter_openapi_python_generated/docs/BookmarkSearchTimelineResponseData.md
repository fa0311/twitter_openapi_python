# BookmarkSearchTimelineResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_by_raw_query** | [**BookmarkSearch**](BookmarkSearch.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.bookmark_search_timeline_response_data import BookmarkSearchTimelineResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkSearchTimelineResponseData from a JSON string
bookmark_search_timeline_response_data_instance = BookmarkSearchTimelineResponseData.from_json(json)
# print the JSON string representation of the object
print(BookmarkSearchTimelineResponseData.to_json())

# convert the object into a dict
bookmark_search_timeline_response_data_dict = bookmark_search_timeline_response_data_instance.to_dict()
# create an instance of BookmarkSearchTimelineResponseData from a dict
bookmark_search_timeline_response_data_from_dict = BookmarkSearchTimelineResponseData.from_dict(bookmark_search_timeline_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



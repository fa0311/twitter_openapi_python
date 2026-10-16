# BookmarkSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks_search_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.bookmark_search import BookmarkSearch

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkSearch from a JSON string
bookmark_search_instance = BookmarkSearch.from_json(json)
# print the JSON string representation of the object
print(BookmarkSearch.to_json())

# convert the object into a dict
bookmark_search_dict = bookmark_search_instance.to_dict()
# create an instance of BookmarkSearch from a dict
bookmark_search_from_dict = BookmarkSearch.from_dict(bookmark_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



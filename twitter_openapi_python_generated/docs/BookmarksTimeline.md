# BookmarksTimeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**Timeline**](Timeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.bookmarks_timeline import BookmarksTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarksTimeline from a JSON string
bookmarks_timeline_instance = BookmarksTimeline.from_json(json)
# print the JSON string representation of the object
print BookmarksTimeline.to_json()

# convert the object into a dict
bookmarks_timeline_dict = bookmarks_timeline_instance.to_dict()
# create an instance of BookmarksTimeline from a dict
bookmarks_timeline_form_dict = bookmarks_timeline.from_dict(bookmarks_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BookmarksResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_timeline_v2** | [**BookmarksTimeline**](BookmarksTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.bookmarks_response_data import BookmarksResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarksResponseData from a JSON string
bookmarks_response_data_instance = BookmarksResponseData.from_json(json)
# print the JSON string representation of the object
print BookmarksResponseData.to_json()

# convert the object into a dict
bookmarks_response_data_dict = bookmarks_response_data_instance.to_dict()
# create an instance of BookmarksResponseData from a dict
bookmarks_response_data_form_dict = bookmarks_response_data.from_dict(bookmarks_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



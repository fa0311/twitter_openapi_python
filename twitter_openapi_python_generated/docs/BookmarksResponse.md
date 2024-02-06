# BookmarksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BookmarksResponseData**](BookmarksResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.bookmarks_response import BookmarksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarksResponse from a JSON string
bookmarks_response_instance = BookmarksResponse.from_json(json)
# print the JSON string representation of the object
print BookmarksResponse.to_json()

# convert the object into a dict
bookmarks_response_dict = bookmarks_response_instance.to_dict()
# create an instance of BookmarksResponse from a dict
bookmarks_response_form_dict = bookmarks_response.from_dict(bookmarks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



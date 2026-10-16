# BookmarkSearchTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BookmarkSearchTimelineResponseData**](BookmarkSearchTimelineResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.bookmark_search_timeline_response import BookmarkSearchTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkSearchTimelineResponse from a JSON string
bookmark_search_timeline_response_instance = BookmarkSearchTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(BookmarkSearchTimelineResponse.to_json())

# convert the object into a dict
bookmark_search_timeline_response_dict = bookmark_search_timeline_response_instance.to_dict()
# create an instance of BookmarkSearchTimelineResponse from a dict
bookmark_search_timeline_response_from_dict = BookmarkSearchTimelineResponse.from_dict(bookmark_search_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListsManagementPageTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListsManagementPageTimelineResponseData**](ListsManagementPageTimelineResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.lists_management_page_timeline_response import ListsManagementPageTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListsManagementPageTimelineResponse from a JSON string
lists_management_page_timeline_response_instance = ListsManagementPageTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(ListsManagementPageTimelineResponse.to_json())

# convert the object into a dict
lists_management_page_timeline_response_dict = lists_management_page_timeline_response_instance.to_dict()
# create an instance of ListsManagementPageTimelineResponse from a dict
lists_management_page_timeline_response_from_dict = ListsManagementPageTimelineResponse.from_dict(lists_management_page_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



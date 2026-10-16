# ListsManagementViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_management_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.lists_management_viewer import ListsManagementViewer

# TODO update the JSON string below
json = "{}"
# create an instance of ListsManagementViewer from a JSON string
lists_management_viewer_instance = ListsManagementViewer.from_json(json)
# print the JSON string representation of the object
print(ListsManagementViewer.to_json())

# convert the object into a dict
lists_management_viewer_dict = lists_management_viewer_instance.to_dict()
# create an instance of ListsManagementViewer from a dict
lists_management_viewer_from_dict = ListsManagementViewer.from_dict(lists_management_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



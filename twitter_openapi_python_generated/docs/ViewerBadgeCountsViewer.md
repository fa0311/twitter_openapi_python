# ViewerBadgeCountsViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_results** | [**ViewerBadgeCountsUserResults**](ViewerBadgeCountsUserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.viewer_badge_counts_viewer import ViewerBadgeCountsViewer

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerBadgeCountsViewer from a JSON string
viewer_badge_counts_viewer_instance = ViewerBadgeCountsViewer.from_json(json)
# print the JSON string representation of the object
print(ViewerBadgeCountsViewer.to_json())

# convert the object into a dict
viewer_badge_counts_viewer_dict = viewer_badge_counts_viewer_instance.to_dict()
# create an instance of ViewerBadgeCountsViewer from a dict
viewer_badge_counts_viewer_from_dict = ViewerBadgeCountsViewer.from_dict(viewer_badge_counts_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



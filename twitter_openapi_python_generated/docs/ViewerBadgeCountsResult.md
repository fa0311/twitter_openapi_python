# ViewerBadgeCountsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**badge_counts** | [**BadgeCounts**](BadgeCounts.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.viewer_badge_counts_result import ViewerBadgeCountsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerBadgeCountsResult from a JSON string
viewer_badge_counts_result_instance = ViewerBadgeCountsResult.from_json(json)
# print the JSON string representation of the object
print(ViewerBadgeCountsResult.to_json())

# convert the object into a dict
viewer_badge_counts_result_dict = viewer_badge_counts_result_instance.to_dict()
# create an instance of ViewerBadgeCountsResult from a dict
viewer_badge_counts_result_from_dict = ViewerBadgeCountsResult.from_dict(viewer_badge_counts_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



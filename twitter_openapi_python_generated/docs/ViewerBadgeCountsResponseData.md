# ViewerBadgeCountsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer_v2** | [**ViewerBadgeCountsViewer**](ViewerBadgeCountsViewer.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.viewer_badge_counts_response_data import ViewerBadgeCountsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerBadgeCountsResponseData from a JSON string
viewer_badge_counts_response_data_instance = ViewerBadgeCountsResponseData.from_json(json)
# print the JSON string representation of the object
print(ViewerBadgeCountsResponseData.to_json())

# convert the object into a dict
viewer_badge_counts_response_data_dict = viewer_badge_counts_response_data_instance.to_dict()
# create an instance of ViewerBadgeCountsResponseData from a dict
viewer_badge_counts_response_data_from_dict = ViewerBadgeCountsResponseData.from_dict(viewer_badge_counts_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



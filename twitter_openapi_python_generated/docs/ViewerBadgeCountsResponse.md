# ViewerBadgeCountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ViewerBadgeCountsResponseData**](ViewerBadgeCountsResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.viewer_badge_counts_response import ViewerBadgeCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerBadgeCountsResponse from a JSON string
viewer_badge_counts_response_instance = ViewerBadgeCountsResponse.from_json(json)
# print the JSON string representation of the object
print(ViewerBadgeCountsResponse.to_json())

# convert the object into a dict
viewer_badge_counts_response_dict = viewer_badge_counts_response_instance.to_dict()
# create an instance of ViewerBadgeCountsResponse from a dict
viewer_badge_counts_response_from_dict = ViewerBadgeCountsResponse.from_dict(viewer_badge_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



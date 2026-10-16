# CommunityDiscoveryTimelineResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer** | [**CommunityDiscoveryTimelineViewer**](CommunityDiscoveryTimelineViewer.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_discovery_timeline_response_data import CommunityDiscoveryTimelineResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityDiscoveryTimelineResponseData from a JSON string
community_discovery_timeline_response_data_instance = CommunityDiscoveryTimelineResponseData.from_json(json)
# print the JSON string representation of the object
print(CommunityDiscoveryTimelineResponseData.to_json())

# convert the object into a dict
community_discovery_timeline_response_data_dict = community_discovery_timeline_response_data_instance.to_dict()
# create an instance of CommunityDiscoveryTimelineResponseData from a dict
community_discovery_timeline_response_data_from_dict = CommunityDiscoveryTimelineResponseData.from_dict(community_discovery_timeline_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



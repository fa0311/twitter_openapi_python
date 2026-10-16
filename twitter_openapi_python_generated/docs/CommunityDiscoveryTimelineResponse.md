# CommunityDiscoveryTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunityDiscoveryTimelineResponseData**](CommunityDiscoveryTimelineResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_discovery_timeline_response import CommunityDiscoveryTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityDiscoveryTimelineResponse from a JSON string
community_discovery_timeline_response_instance = CommunityDiscoveryTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityDiscoveryTimelineResponse.to_json())

# convert the object into a dict
community_discovery_timeline_response_dict = community_discovery_timeline_response_instance.to_dict()
# create an instance of CommunityDiscoveryTimelineResponse from a dict
community_discovery_timeline_response_from_dict = CommunityDiscoveryTimelineResponse.from_dict(community_discovery_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



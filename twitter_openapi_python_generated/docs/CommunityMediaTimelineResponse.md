# CommunityMediaTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MediaCommunityTweetData**](MediaCommunityTweetData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_media_timeline_response import CommunityMediaTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMediaTimelineResponse from a JSON string
community_media_timeline_response_instance = CommunityMediaTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityMediaTimelineResponse.to_json())

# convert the object into a dict
community_media_timeline_response_dict = community_media_timeline_response_instance.to_dict()
# create an instance of CommunityMediaTimelineResponse from a dict
community_media_timeline_response_from_dict = CommunityMediaTimelineResponse.from_dict(community_media_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



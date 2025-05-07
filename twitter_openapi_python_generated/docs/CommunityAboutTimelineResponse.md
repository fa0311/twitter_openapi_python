# CommunityAboutTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AboutCommunityTweetData**](AboutCommunityTweetData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_about_timeline_response import CommunityAboutTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityAboutTimelineResponse from a JSON string
community_about_timeline_response_instance = CommunityAboutTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityAboutTimelineResponse.to_json())

# convert the object into a dict
community_about_timeline_response_dict = community_about_timeline_response_instance.to_dict()
# create an instance of CommunityAboutTimelineResponse from a dict
community_about_timeline_response_from_dict = CommunityAboutTimelineResponse.from_dict(community_about_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



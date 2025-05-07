# CommunityTweetsTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RankedCommunityTweetData**](RankedCommunityTweetData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_tweets_timeline_response import CommunityTweetsTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityTweetsTimelineResponse from a JSON string
community_tweets_timeline_response_instance = CommunityTweetsTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityTweetsTimelineResponse.to_json())

# convert the object into a dict
community_tweets_timeline_response_dict = community_tweets_timeline_response_instance.to_dict()
# create an instance of CommunityTweetsTimelineResponse from a dict
community_tweets_timeline_response_from_dict = CommunityTweetsTimelineResponse.from_dict(community_tweets_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



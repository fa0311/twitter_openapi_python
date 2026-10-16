# GlobalCommunitiesLatestPostSearchTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GlobalCommunitiesLatestPostSearchTimelineResponseData**](GlobalCommunitiesLatestPostSearchTimelineResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.global_communities_latest_post_search_timeline_response import GlobalCommunitiesLatestPostSearchTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalCommunitiesLatestPostSearchTimelineResponse from a JSON string
global_communities_latest_post_search_timeline_response_instance = GlobalCommunitiesLatestPostSearchTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(GlobalCommunitiesLatestPostSearchTimelineResponse.to_json())

# convert the object into a dict
global_communities_latest_post_search_timeline_response_dict = global_communities_latest_post_search_timeline_response_instance.to_dict()
# create an instance of GlobalCommunitiesLatestPostSearchTimelineResponse from a dict
global_communities_latest_post_search_timeline_response_from_dict = GlobalCommunitiesLatestPostSearchTimelineResponse.from_dict(global_communities_latest_post_search_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



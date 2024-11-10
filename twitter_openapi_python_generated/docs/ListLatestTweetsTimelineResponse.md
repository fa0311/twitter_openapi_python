# ListLatestTweetsTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListTweetsTimelineData**](ListTweetsTimelineData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.list_latest_tweets_timeline_response import ListLatestTweetsTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestTweetsTimelineResponse from a JSON string
list_latest_tweets_timeline_response_instance = ListLatestTweetsTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(ListLatestTweetsTimelineResponse.to_json())

# convert the object into a dict
list_latest_tweets_timeline_response_dict = list_latest_tweets_timeline_response_instance.to_dict()
# create an instance of ListLatestTweetsTimelineResponse from a dict
list_latest_tweets_timeline_response_from_dict = ListLatestTweetsTimelineResponse.from_dict(list_latest_tweets_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



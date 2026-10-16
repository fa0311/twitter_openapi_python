# FetchScheduledTweetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FetchScheduledTweetsResponseData**](FetchScheduledTweetsResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.fetch_scheduled_tweets_response import FetchScheduledTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchScheduledTweetsResponse from a JSON string
fetch_scheduled_tweets_response_instance = FetchScheduledTweetsResponse.from_json(json)
# print the JSON string representation of the object
print(FetchScheduledTweetsResponse.to_json())

# convert the object into a dict
fetch_scheduled_tweets_response_dict = fetch_scheduled_tweets_response_instance.to_dict()
# create an instance of FetchScheduledTweetsResponse from a dict
fetch_scheduled_tweets_response_from_dict = FetchScheduledTweetsResponse.from_dict(fetch_scheduled_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



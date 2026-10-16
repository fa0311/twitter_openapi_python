# FetchScheduledTweetsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer** | [**ScheduledTweetsViewer**](ScheduledTweetsViewer.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.fetch_scheduled_tweets_response_data import FetchScheduledTweetsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FetchScheduledTweetsResponseData from a JSON string
fetch_scheduled_tweets_response_data_instance = FetchScheduledTweetsResponseData.from_json(json)
# print the JSON string representation of the object
print(FetchScheduledTweetsResponseData.to_json())

# convert the object into a dict
fetch_scheduled_tweets_response_data_dict = fetch_scheduled_tweets_response_data_instance.to_dict()
# create an instance of FetchScheduledTweetsResponseData from a dict
fetch_scheduled_tweets_response_data_from_dict = FetchScheduledTweetsResponseData.from_dict(fetch_scheduled_tweets_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



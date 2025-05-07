# ListTweetsTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ListTweetsTimelineList**](ListTweetsTimelineList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_tweets_timeline_data import ListTweetsTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of ListTweetsTimelineData from a JSON string
list_tweets_timeline_data_instance = ListTweetsTimelineData.from_json(json)
# print the JSON string representation of the object
print(ListTweetsTimelineData.to_json())

# convert the object into a dict
list_tweets_timeline_data_dict = list_tweets_timeline_data_instance.to_dict()
# create an instance of ListTweetsTimelineData from a dict
list_tweets_timeline_data_from_dict = ListTweetsTimelineData.from_dict(list_tweets_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListTweetsTimeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**Timeline**](Timeline.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.list_tweets_timeline import ListTweetsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of ListTweetsTimeline from a JSON string
list_tweets_timeline_instance = ListTweetsTimeline.from_json(json)
# print the JSON string representation of the object
print ListTweetsTimeline.to_json()

# convert the object into a dict
list_tweets_timeline_dict = list_tweets_timeline_instance.to_dict()
# create an instance of ListTweetsTimeline from a dict
list_tweets_timeline_form_dict = list_tweets_timeline.from_dict(list_tweets_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



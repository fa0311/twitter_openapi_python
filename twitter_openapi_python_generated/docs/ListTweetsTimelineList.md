# ListTweetsTimelineList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweets_timeline** | [**ListTweetsTimeline**](ListTweetsTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_tweets_timeline_list import ListTweetsTimelineList

# TODO update the JSON string below
json = "{}"
# create an instance of ListTweetsTimelineList from a JSON string
list_tweets_timeline_list_instance = ListTweetsTimelineList.from_json(json)
# print the JSON string representation of the object
print ListTweetsTimelineList.to_json()

# convert the object into a dict
list_tweets_timeline_list_dict = list_tweets_timeline_list_instance.to_dict()
# create an instance of ListTweetsTimelineList from a dict
list_tweets_timeline_list_form_dict = list_tweets_timeline_list.from_dict(list_tweets_timeline_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



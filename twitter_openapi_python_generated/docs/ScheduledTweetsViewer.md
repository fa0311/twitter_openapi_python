# ScheduledTweetsViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_tweet_list** | **List[Dict[str, object]]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.scheduled_tweets_viewer import ScheduledTweetsViewer

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTweetsViewer from a JSON string
scheduled_tweets_viewer_instance = ScheduledTweetsViewer.from_json(json)
# print the JSON string representation of the object
print(ScheduledTweetsViewer.to_json())

# convert the object into a dict
scheduled_tweets_viewer_dict = scheduled_tweets_viewer_instance.to_dict()
# create an instance of ScheduledTweetsViewer from a dict
scheduled_tweets_viewer_from_dict = ScheduledTweetsViewer.from_dict(scheduled_tweets_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



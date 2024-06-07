# UserHighlightsTweetsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**Timeline**](Timeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_tweets_timeline import UserHighlightsTweetsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsTweetsTimeline from a JSON string
user_highlights_tweets_timeline_instance = UserHighlightsTweetsTimeline.from_json(json)
# print the JSON string representation of the object
print(UserHighlightsTweetsTimeline.to_json())

# convert the object into a dict
user_highlights_tweets_timeline_dict = user_highlights_tweets_timeline_instance.to_dict()
# create an instance of UserHighlightsTweetsTimeline from a dict
user_highlights_tweets_timeline_from_dict = UserHighlightsTweetsTimeline.from_dict(user_highlights_tweets_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



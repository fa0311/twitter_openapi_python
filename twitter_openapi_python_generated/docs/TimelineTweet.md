# TimelineTweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**highlights** | [**Highlight**](Highlight.md) |  | [optional] 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**promoted_metadata** | **Dict[str, object]** |  | [optional] 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**tweet_display_type** | **str** |  | 
**tweet_results** | [**ItemResult**](ItemResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_tweet import TimelineTweet

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTweet from a JSON string
timeline_tweet_instance = TimelineTweet.from_json(json)
# print the JSON string representation of the object
print(TimelineTweet.to_json())

# convert the object into a dict
timeline_tweet_dict = timeline_tweet_instance.to_dict()
# create an instance of TimelineTweet from a dict
timeline_tweet_form_dict = timeline_tweet.from_dict(timeline_tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



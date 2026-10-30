# TweetSportsPostContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitors** | [**List[TweetSportsCompetitor]**](TweetSportsCompetitor.md) |  | 
**game_id** | [**TweetSportsRestId**](TweetSportsRestId.md) |  | 
**league** | **str** |  | 
**scheduled_at_ms** | **str** |  | 
**state** | **str** |  | 
**status_text** | **str** |  | 
**title** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_sports_post_context import TweetSportsPostContext

# TODO update the JSON string below
json = "{}"
# create an instance of TweetSportsPostContext from a JSON string
tweet_sports_post_context_instance = TweetSportsPostContext.from_json(json)
# print the JSON string representation of the object
print(TweetSportsPostContext.to_json())

# convert the object into a dict
tweet_sports_post_context_dict = tweet_sports_post_context_instance.to_dict()
# create an instance of TweetSportsPostContext from a dict
tweet_sports_post_context_from_dict = TweetSportsPostContext.from_dict(tweet_sports_post_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



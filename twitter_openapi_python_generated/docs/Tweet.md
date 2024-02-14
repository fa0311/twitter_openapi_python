# Tweet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**author_community_relationship** | [**AuthorCommunityRelationship**](AuthorCommunityRelationship.md) |  | [optional] 
**birdwatch_pivot** | [**BirdwatchPivot**](BirdwatchPivot.md) |  | [optional] 
**card** | [**TweetCard**](TweetCard.md) |  | [optional] 
**core** | [**UserResultCore**](UserResultCore.md) |  | [optional] 
**edit_control** | [**TweetEditControl**](TweetEditControl.md) |  | [optional] 
**edit_prespective** | [**TweetEditPrespective**](TweetEditPrespective.md) |  | [optional] 
**has_birdwatch_notes** | **bool** |  | [optional] 
**is_translatable** | **bool** |  | [optional] [default to False]
**legacy** | [**TweetLegacy**](TweetLegacy.md) |  | [optional] 
**note_tweet** | [**NoteTweet**](NoteTweet.md) |  | [optional] 
**previous_counts** | [**TweetPreviousCounts**](TweetPreviousCounts.md) |  | [optional] 
**quick_promote_eligibility** | **object** |  | [optional] 
**quoted_ref_result** | [**QuotedRefResult**](QuotedRefResult.md) |  | [optional] 
**quoted_status_result** | [**ItemResult**](ItemResult.md) |  | [optional] 
**rest_id** | **str** |  | 
**source** | **str** |  | [optional] 
**super_follows_reply_user_result** | [**SuperFollowsReplyUserResult**](SuperFollowsReplyUserResult.md) |  | [optional] 
**unified_card** | [**UnifiedCard**](UnifiedCard.md) |  | [optional] 
**unmention_data** | **Dict[str, object]** |  | [optional] 
**views** | [**TweetView**](TweetView.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tweet import Tweet

# TODO update the JSON string below
json = "{}"
# create an instance of Tweet from a JSON string
tweet_instance = Tweet.from_json(json)
# print the JSON string representation of the object
print Tweet.to_json()

# convert the object into a dict
tweet_dict = tweet_instance.to_dict()
# create an instance of Tweet from a dict
tweet_form_dict = tweet.from_dict(tweet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TweetUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**article** | [**Article**](Article.md) |  | [optional] 
**author_community_relationship** | [**AuthorCommunityRelationship**](AuthorCommunityRelationship.md) |  | [optional] 
**birdwatch_pivot** | [**BirdwatchPivot**](BirdwatchPivot.md) |  | [optional] 
**card** | [**TweetCard**](TweetCard.md) |  | [optional] 
**community_relationship** | [**CommunityRelationship**](CommunityRelationship.md) |  | [optional] 
**community_results** | [**Community**](Community.md) |  | [optional] 
**core** | [**UserResultCore**](UserResultCore.md) |  | [optional] 
**edit_control** | [**TweetEditControl**](TweetEditControl.md) |  | [optional] 
**edit_prespective** | [**TweetEditPrespective**](TweetEditPrespective.md) |  | [optional] 
**grok_analysis_followups** | **List[str]** |  | [optional] 
**grok_share_attachment** | [**GrokShareAttachment**](GrokShareAttachment.md) |  | [optional] 
**has_birdwatch_notes** | **bool** |  | [optional] 
**is_translatable** | **bool** |  | [optional] 
**legacy** | [**TweetLegacy**](TweetLegacy.md) |  | [optional] 
**note_tweet** | [**NoteTweet**](NoteTweet.md) |  | [optional] 
**previous_counts** | [**TweetPreviousCounts**](TweetPreviousCounts.md) |  | [optional] 
**quick_promote_eligibility** | **object** |  | [optional] 
**quoted_ref_result** | [**QuotedRefResult**](QuotedRefResult.md) |  | [optional] 
**quoted_status_result** | [**ItemResult**](ItemResult.md) |  | [optional] 
**rest_id** | **str** |  | 
**source** | **str** |  | [optional] 
**super_follows_reply_user_result** | [**SuperFollowsReplyUserResult**](SuperFollowsReplyUserResult.md) |  | [optional] 
**trend_results** | [**TrendResults**](TrendResults.md) |  | [optional] 
**unified_card** | [**UnifiedCard**](UnifiedCard.md) |  | [optional] 
**unmention_data** | **Dict[str, object]** |  | [optional] 
**views** | [**TweetView**](TweetView.md) |  | [optional] 
**limited_action_results** | **Dict[str, object]** |  | [optional] 
**media_visibility_results** | [**MediaVisibilityResults**](MediaVisibilityResults.md) |  | [optional] 
**tweet** | [**TweetPreviewDisplayTweet**](TweetPreviewDisplayTweet.md) |  | 
**tweet_interstitial** | [**TweetInterstitial**](TweetInterstitial.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**cta** | [**TweetPreviewDisplayCta**](TweetPreviewDisplayCta.md) |  | 
**limited_action_results** | [**TweetLimitedActionResults**](TweetLimitedActionResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_union import TweetUnion

# TODO update the JSON string below
json = "{}"
# create an instance of TweetUnion from a JSON string
tweet_union_instance = TweetUnion.from_json(json)
# print the JSON string representation of the object
print(TweetUnion.to_json())

# convert the object into a dict
tweet_union_dict = tweet_union_instance.to_dict()
# create an instance of TweetUnion from a dict
tweet_union_from_dict = TweetUnion.from_dict(tweet_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



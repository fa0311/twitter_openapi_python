# TweetLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmark_count** | **int** |  | 
**bookmarked** | **bool** |  | 
**conversation_control** | **Dict[str, object]** |  | [optional] 
**conversation_id_str** | **str** |  | 
**created_at** | **str** |  | 
**display_text_range** | **List[int]** |  | 
**entities** | [**Entities**](Entities.md) |  | 
**extended_entities** | [**ExtendedEntities**](ExtendedEntities.md) |  | [optional] 
**favorite_count** | **int** |  | 
**favorited** | **bool** |  | 
**full_text** | **str** |  | 
**id_str** | **str** |  | 
**in_reply_to_screen_name** | **str** |  | [optional] 
**in_reply_to_status_id_str** | **str** |  | [optional] 
**in_reply_to_user_id_str** | **str** |  | [optional] 
**is_quote_status** | **bool** |  | 
**lang** | **str** |  | 
**limited_actions** | **str** |  | [optional] 
**place** | **Dict[str, object]** |  | [optional] 
**possibly_sensitive** | **bool** |  | [optional] [default to False]
**possibly_sensitive_editable** | **bool** |  | [optional] [default to False]
**quote_count** | **int** |  | 
**quoted_status_id_str** | **str** |  | [optional] 
**quoted_status_permalink** | [**QuotedStatusPermalink**](QuotedStatusPermalink.md) |  | [optional] 
**reply_count** | **int** |  | 
**retweet_count** | **int** |  | 
**retweeted** | **bool** |  | 
**retweeted_status_result** | [**ItemResult**](ItemResult.md) |  | [optional] 
**scopes** | [**TweetLegacyScopes**](TweetLegacyScopes.md) |  | [optional] 
**self_thread** | [**SelfThread**](SelfThread.md) |  | [optional] 
**user_id_str** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.tweet_legacy import TweetLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of TweetLegacy from a JSON string
tweet_legacy_instance = TweetLegacy.from_json(json)
# print the JSON string representation of the object
print(TweetLegacy.to_json())

# convert the object into a dict
tweet_legacy_dict = tweet_legacy_instance.to_dict()
# create an instance of TweetLegacy from a dict
tweet_legacy_form_dict = tweet_legacy.from_dict(tweet_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ItemContentUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**has_moderated_replies** | **bool** |  | [optional] 
**highlights** | [**Highlight**](Highlight.md) |  | [optional] 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**promoted_metadata** | **Dict[str, object]** |  | [optional] 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**tweet_display_type** | **str** |  | 
**tweet_results** | [**ItemResult**](ItemResult.md) |  | 
**cursor_type** | [**CursorType**](CursorType.md) |  | 
**display_treatment** | [**DisplayTreatment**](DisplayTreatment.md) |  | [optional] 
**entry_type** | [**ContentEntryType**](ContentEntryType.md) |  | [optional] 
**stop_on_empty_response** | **bool** |  | [optional] 
**value** | **str** |  | 
**user_display_type** | **str** |  | 
**user_results** | [**UserResults**](UserResults.md) |  | 
**tombstone_display_type** | **str** |  | [optional] 
**tombstone_info** | [**TombstoneInfo**](TombstoneInfo.md) |  | [optional] 
**images** | [**List[TrendImage]**](TrendImage.md) |  | [optional] 
**is_ai_trend** | **bool** |  | [optional] 
**name** | **str** |  | 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**thumbnail_image** | [**ThumbnailImage**](ThumbnailImage.md) |  | [optional] 
**trend_metadata** | [**TrendMetadata**](TrendMetadata.md) |  | 
**trend_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 
**id** | **str** |  | 
**notification_icon** | **str** |  | 
**notification_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 
**rich_message** | [**RichMessage**](RichMessage.md) |  | 
**template** | [**NotificationTemplate**](NotificationTemplate.md) |  | 
**timestamp_ms** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.item_content_union import ItemContentUnion

# TODO update the JSON string below
json = "{}"
# create an instance of ItemContentUnion from a JSON string
item_content_union_instance = ItemContentUnion.from_json(json)
# print the JSON string representation of the object
print(ItemContentUnion.to_json())

# convert the object into a dict
item_content_union_dict = item_content_union_instance.to_dict()
# create an instance of ItemContentUnion from a dict
item_content_union_from_dict = ItemContentUnion.from_dict(item_content_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



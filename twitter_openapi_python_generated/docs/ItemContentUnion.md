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



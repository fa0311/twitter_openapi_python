# ContentUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**client_event_info** | **Dict[str, object]** |  | 
**entry_type** | [**ContentEntryType**](ContentEntryType.md) |  | 
**feedback_info** | [**FeedbackInfo**](FeedbackInfo.md) |  | [optional] 
**item_content** | [**ItemContentUnion**](ItemContentUnion.md) |  | 
**display_type** | [**DisplayType**](DisplayType.md) |  | 
**footer** | **Dict[str, object]** |  | [optional] 
**header** | **Dict[str, object]** |  | [optional] 
**items** | [**List[ModuleItem]**](ModuleItem.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**cursor_type** | [**CursorType**](CursorType.md) |  | 
**display_treatment** | [**DisplayTreatment**](DisplayTreatment.md) |  | [optional] 
**item_type** | [**ContentEntryType**](ContentEntryType.md) |  | [optional] 
**stop_on_empty_response** | **bool** |  | [default to False]
**value** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.content_union import ContentUnion

# TODO update the JSON string below
json = "{}"
# create an instance of ContentUnion from a JSON string
content_union_instance = ContentUnion.from_json(json)
# print the JSON string representation of the object
print(ContentUnion.to_json())

# convert the object into a dict
content_union_dict = content_union_instance.to_dict()
# create an instance of ContentUnion from a dict
content_union_form_dict = content_union.from_dict(content_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



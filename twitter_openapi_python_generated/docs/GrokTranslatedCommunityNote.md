# GrokTranslatedCommunityNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_language** | **str** |  | 
**rich_text_entities** | [**List[GrokEntity]**](GrokEntity.md) |  | [optional] 
**source_language** | **str** |  | 
**translation** | **str** |  | 
**translation_available** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_translated_community_note import GrokTranslatedCommunityNote

# TODO update the JSON string below
json = "{}"
# create an instance of GrokTranslatedCommunityNote from a JSON string
grok_translated_community_note_instance = GrokTranslatedCommunityNote.from_json(json)
# print the JSON string representation of the object
print(GrokTranslatedCommunityNote.to_json())

# convert the object into a dict
grok_translated_community_note_dict = grok_translated_community_note_instance.to_dict()
# create an instance of GrokTranslatedCommunityNote from a dict
grok_translated_community_note_from_dict = GrokTranslatedCommunityNote.from_dict(grok_translated_community_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



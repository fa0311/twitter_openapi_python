# GrokTranslatedPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_data** | **Dict[str, object]** |  | [optional] 
**destination_language** | **str** |  | [optional] 
**entities** | [**Entities**](Entities.md) |  | [optional] 
**preview_translation** | **str** |  | [optional] 
**source_language** | **str** |  | [optional] 
**translation** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.grok_translated_post import GrokTranslatedPost

# TODO update the JSON string below
json = "{}"
# create an instance of GrokTranslatedPost from a JSON string
grok_translated_post_instance = GrokTranslatedPost.from_json(json)
# print the JSON string representation of the object
print(GrokTranslatedPost.to_json())

# convert the object into a dict
grok_translated_post_dict = grok_translated_post_instance.to_dict()
# create an instance of GrokTranslatedPost from a dict
grok_translated_post_from_dict = GrokTranslatedPost.from_dict(grok_translated_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



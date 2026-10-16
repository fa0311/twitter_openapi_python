# GrokTranslatedBio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_language** | **str** |  | 
**entities** | [**Entities**](Entities.md) |  | 
**source_language** | **str** |  | 
**translation** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_translated_bio import GrokTranslatedBio

# TODO update the JSON string below
json = "{}"
# create an instance of GrokTranslatedBio from a JSON string
grok_translated_bio_instance = GrokTranslatedBio.from_json(json)
# print the JSON string representation of the object
print(GrokTranslatedBio.to_json())

# convert the object into a dict
grok_translated_bio_dict = grok_translated_bio_instance.to_dict()
# create an instance of GrokTranslatedBio from a dict
grok_translated_bio_from_dict = GrokTranslatedBio.from_dict(grok_translated_bio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



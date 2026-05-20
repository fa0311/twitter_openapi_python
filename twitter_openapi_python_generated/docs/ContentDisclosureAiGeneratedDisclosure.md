# ContentDisclosureAiGeneratedDisclosure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_generated_detection_source** | **str** |  | [optional] 
**can_edit** | **bool** |  | 
**has_ai_generated_media** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.content_disclosure_ai_generated_disclosure import ContentDisclosureAiGeneratedDisclosure

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDisclosureAiGeneratedDisclosure from a JSON string
content_disclosure_ai_generated_disclosure_instance = ContentDisclosureAiGeneratedDisclosure.from_json(json)
# print the JSON string representation of the object
print(ContentDisclosureAiGeneratedDisclosure.to_json())

# convert the object into a dict
content_disclosure_ai_generated_disclosure_dict = content_disclosure_ai_generated_disclosure_instance.to_dict()
# create an instance of ContentDisclosureAiGeneratedDisclosure from a dict
content_disclosure_ai_generated_disclosure_from_dict = ContentDisclosureAiGeneratedDisclosure.from_dict(content_disclosure_ai_generated_disclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



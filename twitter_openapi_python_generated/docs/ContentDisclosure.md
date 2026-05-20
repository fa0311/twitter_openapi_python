# ContentDisclosure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertising_disclosure** | [**ContentDisclosureAdvertisingDisclosure**](ContentDisclosureAdvertisingDisclosure.md) |  | [optional] 
**ai_generated_disclosure** | [**ContentDisclosureAiGeneratedDisclosure**](ContentDisclosureAiGeneratedDisclosure.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.content_disclosure import ContentDisclosure

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDisclosure from a JSON string
content_disclosure_instance = ContentDisclosure.from_json(json)
# print the JSON string representation of the object
print(ContentDisclosure.to_json())

# convert the object into a dict
content_disclosure_dict = content_disclosure_instance.to_dict()
# create an instance of ContentDisclosure from a dict
content_disclosure_from_dict = ContentDisclosure.from_dict(content_disclosure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



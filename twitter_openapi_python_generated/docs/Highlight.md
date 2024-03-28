# Highlight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_highlights** | [**List[TextHighlight]**](TextHighlight.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.highlight import Highlight

# TODO update the JSON string below
json = "{}"
# create an instance of Highlight from a JSON string
highlight_instance = Highlight.from_json(json)
# print the JSON string representation of the object
print(Highlight.to_json())

# convert the object into a dict
highlight_dict = highlight_instance.to_dict()
# create an instance of Highlight from a dict
highlight_form_dict = highlight.from_dict(highlight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



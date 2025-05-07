# GrokImageAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**upsampled_prompt** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.grok_image_annotation import GrokImageAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of GrokImageAnnotation from a JSON string
grok_image_annotation_instance = GrokImageAnnotation.from_json(json)
# print the JSON string representation of the object
print(GrokImageAnnotation.to_json())

# convert the object into a dict
grok_image_annotation_dict = grok_image_annotation_instance.to_dict()
# create an instance of GrokImageAnnotation from a dict
grok_image_annotation_from_dict = GrokImageAnnotation.from_dict(grok_image_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



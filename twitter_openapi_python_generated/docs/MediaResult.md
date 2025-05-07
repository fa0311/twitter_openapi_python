# MediaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grok_image_annotation** | [**GrokImageAnnotation**](GrokImageAnnotation.md) |  | [optional] 
**media_key** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_result import MediaResult

# TODO update the JSON string below
json = "{}"
# create an instance of MediaResult from a JSON string
media_result_instance = MediaResult.from_json(json)
# print the JSON string representation of the object
print(MediaResult.to_json())

# convert the object into a dict
media_result_dict = media_result_instance.to_dict()
# create an instance of MediaResult from a dict
media_result_from_dict = MediaResult.from_dict(media_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PrerollVideoVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitrate** | **int** |  | 
**content_type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.preroll_video_variant import PrerollVideoVariant

# TODO update the JSON string below
json = "{}"
# create an instance of PrerollVideoVariant from a JSON string
preroll_video_variant_instance = PrerollVideoVariant.from_json(json)
# print the JSON string representation of the object
print(PrerollVideoVariant.to_json())

# convert the object into a dict
preroll_video_variant_dict = preroll_video_variant_instance.to_dict()
# create an instance of PrerollVideoVariant from a dict
preroll_video_variant_from_dict = PrerollVideoVariant.from_dict(preroll_video_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



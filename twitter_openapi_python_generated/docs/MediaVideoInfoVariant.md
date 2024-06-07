# MediaVideoInfoVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitrate** | **int** |  | [optional] 
**content_type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_video_info_variant import MediaVideoInfoVariant

# TODO update the JSON string below
json = "{}"
# create an instance of MediaVideoInfoVariant from a JSON string
media_video_info_variant_instance = MediaVideoInfoVariant.from_json(json)
# print the JSON string representation of the object
print(MediaVideoInfoVariant.to_json())

# convert the object into a dict
media_video_info_variant_dict = media_video_info_variant_instance.to_dict()
# create an instance of MediaVideoInfoVariant from a dict
media_video_info_variant_from_dict = MediaVideoInfoVariant.from_dict(media_video_info_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



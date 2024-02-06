# MediaVideoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **List[int]** |  | 
**duration_millis** | **int** |  | [optional] 
**variants** | [**List[MediaVideoInfoVariant]**](MediaVideoInfoVariant.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_video_info import MediaVideoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaVideoInfo from a JSON string
media_video_info_instance = MediaVideoInfo.from_json(json)
# print the JSON string representation of the object
print MediaVideoInfo.to_json()

# convert the object into a dict
media_video_info_dict = media_video_info_instance.to_dict()
# create an instance of MediaVideoInfo from a dict
media_video_info_form_dict = media_video_info.from_dict(media_video_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MediaColorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**palette** | [**List[MediaColorInfoPalette]**](MediaColorInfoPalette.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_color_info import MediaColorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaColorInfo from a JSON string
media_color_info_instance = MediaColorInfo.from_json(json)
# print the JSON string representation of the object
print(MediaColorInfo.to_json())

# convert the object into a dict
media_color_info_dict = media_color_info_instance.to_dict()
# create an instance of MediaColorInfo from a dict
media_color_info_from_dict = MediaColorInfo.from_dict(media_color_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



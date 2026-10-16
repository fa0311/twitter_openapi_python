# MediaColorInfoPalette


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** |  | 
**rgb** | [**MediaColorInfoPaletteRGB**](MediaColorInfoPaletteRGB.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_color_info_palette import MediaColorInfoPalette

# TODO update the JSON string below
json = "{}"
# create an instance of MediaColorInfoPalette from a JSON string
media_color_info_palette_instance = MediaColorInfoPalette.from_json(json)
# print the JSON string representation of the object
print(MediaColorInfoPalette.to_json())

# convert the object into a dict
media_color_info_palette_dict = media_color_info_palette_instance.to_dict()
# create an instance of MediaColorInfoPalette from a dict
media_color_info_palette_from_dict = MediaColorInfoPalette.from_dict(media_color_info_palette_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



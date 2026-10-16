# ListBannerMediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_img_height** | **int** |  | 
**original_img_url** | **str** |  | 
**original_img_width** | **int** |  | 
**salient_rect** | [**MediaSalientRect**](MediaSalientRect.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_banner_media_info import ListBannerMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ListBannerMediaInfo from a JSON string
list_banner_media_info_instance = ListBannerMediaInfo.from_json(json)
# print the JSON string representation of the object
print(ListBannerMediaInfo.to_json())

# convert the object into a dict
list_banner_media_info_dict = list_banner_media_info_instance.to_dict()
# create an instance of ListBannerMediaInfo from a dict
list_banner_media_info_from_dict = ListBannerMediaInfo.from_dict(list_banner_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



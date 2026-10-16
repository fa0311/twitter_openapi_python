# CommunityBannerMediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**color_info** | [**MediaColorInfo**](MediaColorInfo.md) |  | 
**original_img_height** | **int** |  | 
**original_img_url** | **str** |  | 
**original_img_width** | **int** |  | 
**salient_rect** | [**MediaSalientRect**](MediaSalientRect.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_banner_media_info import CommunityBannerMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityBannerMediaInfo from a JSON string
community_banner_media_info_instance = CommunityBannerMediaInfo.from_json(json)
# print the JSON string representation of the object
print(CommunityBannerMediaInfo.to_json())

# convert the object into a dict
community_banner_media_info_dict = community_banner_media_info_instance.to_dict()
# create an instance of CommunityBannerMediaInfo from a dict
community_banner_media_info_from_dict = CommunityBannerMediaInfo.from_dict(community_banner_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommunityBannerMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**media_info** | [**CommunityBannerMediaInfo**](CommunityBannerMediaInfo.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_banner_media import CommunityBannerMedia

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityBannerMedia from a JSON string
community_banner_media_instance = CommunityBannerMedia.from_json(json)
# print the JSON string representation of the object
print(CommunityBannerMedia.to_json())

# convert the object into a dict
community_banner_media_dict = community_banner_media_instance.to_dict()
# create an instance of CommunityBannerMedia from a dict
community_banner_media_from_dict = CommunityBannerMedia.from_dict(community_banner_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



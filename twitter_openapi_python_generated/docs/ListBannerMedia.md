# ListBannerMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_info** | [**ListBannerMediaInfo**](ListBannerMediaInfo.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_banner_media import ListBannerMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ListBannerMedia from a JSON string
list_banner_media_instance = ListBannerMedia.from_json(json)
# print the JSON string representation of the object
print(ListBannerMedia.to_json())

# convert the object into a dict
list_banner_media_dict = list_banner_media_instance.to_dict()
# create an instance of ListBannerMedia from a dict
list_banner_media_from_dict = ListBannerMedia.from_dict(list_banner_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



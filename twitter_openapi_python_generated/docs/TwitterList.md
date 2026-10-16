# TwitterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**custom_banner_media** | [**ListBannerMedia**](ListBannerMedia.md) |  | [optional] 
**custom_banner_media_results** | [**ListBannerMediaResults**](ListBannerMediaResults.md) |  | [optional] 
**default_banner_media** | [**ListBannerMedia**](ListBannerMedia.md) |  | 
**default_banner_media_results** | [**ListBannerMediaResults**](ListBannerMediaResults.md) |  | 
**description** | **str** |  | 
**facepile_urls** | **List[str]** |  | 
**followers_context** | **str** |  | [optional] 
**following** | **bool** |  | 
**id** | **str** |  | 
**id_str** | **str** |  | 
**is_member** | **bool** |  | 
**member_count** | **int** |  | 
**members_context** | **str** |  | [optional] 
**mode** | **str** |  | 
**muting** | **bool** |  | 
**name** | **str** |  | 
**pinning** | **bool** |  | 
**subscriber_count** | **int** |  | 
**user_results** | [**UserResults**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.twitter_list import TwitterList

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterList from a JSON string
twitter_list_instance = TwitterList.from_json(json)
# print the JSON string representation of the object
print(TwitterList.to_json())

# convert the object into a dict
twitter_list_dict = twitter_list_instance.to_dict()
# create an instance of TwitterList from a dict
twitter_list_from_dict = TwitterList.from_dict(twitter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



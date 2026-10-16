# CommunitySearchCommunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**custom_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | [optional] 
**default_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | 
**id** | **str** |  | 
**is_nsfw** | **bool** |  | 
**member_count** | **int** |  | 
**members_facepile_results** | [**List[CommunityFacepileUserResults]**](CommunityFacepileUserResults.md) |  | 
**name** | **str** |  | 
**primary_community_topic** | [**CommunityPrimaryTopicName**](CommunityPrimaryTopicName.md) |  | [optional] 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_search_community import CommunitySearchCommunity

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySearchCommunity from a JSON string
community_search_community_instance = CommunitySearchCommunity.from_json(json)
# print the JSON string representation of the object
print(CommunitySearchCommunity.to_json())

# convert the object into a dict
community_search_community_dict = community_search_community_instance.to_dict()
# create an instance of CommunitySearchCommunity from a dict
community_search_community_from_dict = CommunitySearchCommunity.from_dict(community_search_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



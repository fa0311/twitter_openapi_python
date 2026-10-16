# CommunityPageCommunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**actions** | [**CommunityPageActions**](CommunityPageActions.md) |  | 
**admin_results** | [**CommunityIdUserResults**](CommunityIdUserResults.md) |  | 
**created_at** | **int** |  | 
**creator_results** | [**CommunityIdUserResults**](CommunityIdUserResults.md) |  | 
**custom_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | 
**default_banner_media** | [**CommunityBannerMedia**](CommunityBannerMedia.md) |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**id_str** | **str** |  | 
**invites_policy** | **str** |  | 
**invites_result** | [**CommunityPageInvitesResult**](CommunityPageInvitesResult.md) |  | 
**is_nsfw** | **bool** |  | 
**is_pinned** | **bool** |  | 
**join_policy** | **str** |  | 
**join_requests_result** | [**CommunityJoinRequestsResult**](CommunityJoinRequestsResult.md) |  | 
**member_count** | **int** |  | 
**members_facepile_results** | [**List[CommunityIdUserResults]**](CommunityIdUserResults.md) |  | 
**moderator_count** | **int** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**rules** | [**List[CommunityRelayRule]**](CommunityRelayRule.md) |  | 
**search_tags** | **List[str]** |  | 
**viewer_relationship** | [**CommunityViewerRelationship**](CommunityViewerRelationship.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_community import CommunityPageCommunity

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageCommunity from a JSON string
community_page_community_instance = CommunityPageCommunity.from_json(json)
# print the JSON string representation of the object
print(CommunityPageCommunity.to_json())

# convert the object into a dict
community_page_community_dict = community_page_community_instance.to_dict()
# create an instance of CommunityPageCommunity from a dict
community_page_community_from_dict = CommunityPageCommunity.from_dict(community_page_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



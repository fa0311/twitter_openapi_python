# CommunityPageInvitesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_community_invites_result** | **str** |  | 
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_invites_result import CommunityPageInvitesResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageInvitesResult from a JSON string
community_page_invites_result_instance = CommunityPageInvitesResult.from_json(json)
# print the JSON string representation of the object
print(CommunityPageInvitesResult.to_json())

# convert the object into a dict
community_page_invites_result_dict = community_page_invites_result_instance.to_dict()
# create an instance of CommunityPageInvitesResult from a dict
community_page_invites_result_from_dict = CommunityPageInvitesResult.from_dict(community_page_invites_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



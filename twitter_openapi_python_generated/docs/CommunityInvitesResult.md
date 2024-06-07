# CommunityInvitesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**message** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_invites_result import CommunityInvitesResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityInvitesResult from a JSON string
community_invites_result_instance = CommunityInvitesResult.from_json(json)
# print the JSON string representation of the object
print(CommunityInvitesResult.to_json())

# convert the object into a dict
community_invites_result_dict = community_invites_result_instance.to_dict()
# create an instance of CommunityInvitesResult from a dict
community_invites_result_from_dict = CommunityInvitesResult.from_dict(community_invites_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



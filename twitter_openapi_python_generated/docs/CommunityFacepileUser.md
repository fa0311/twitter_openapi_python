# CommunityFacepileUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**avatar** | [**UserAvatar**](UserAvatar.md) |  | 
**id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_facepile_user import CommunityFacepileUser

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityFacepileUser from a JSON string
community_facepile_user_instance = CommunityFacepileUser.from_json(json)
# print the JSON string representation of the object
print(CommunityFacepileUser.to_json())

# convert the object into a dict
community_facepile_user_dict = community_facepile_user_instance.to_dict()
# create an instance of CommunityFacepileUser from a dict
community_facepile_user_from_dict = CommunityFacepileUser.from_dict(community_facepile_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



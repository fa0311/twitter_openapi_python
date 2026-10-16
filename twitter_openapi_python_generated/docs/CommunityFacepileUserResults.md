# CommunityFacepileUserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**CommunityFacepileUser**](CommunityFacepileUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_facepile_user_results import CommunityFacepileUserResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityFacepileUserResults from a JSON string
community_facepile_user_results_instance = CommunityFacepileUserResults.from_json(json)
# print the JSON string representation of the object
print(CommunityFacepileUserResults.to_json())

# convert the object into a dict
community_facepile_user_results_dict = community_facepile_user_results_instance.to_dict()
# create an instance of CommunityFacepileUserResults from a dict
community_facepile_user_results_from_dict = CommunityFacepileUserResults.from_dict(community_facepile_user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



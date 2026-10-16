# CommunityIdUserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**UserUnion**](UserUnion.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_id_user_results import CommunityIdUserResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityIdUserResults from a JSON string
community_id_user_results_instance = CommunityIdUserResults.from_json(json)
# print the JSON string representation of the object
print(CommunityIdUserResults.to_json())

# convert the object into a dict
community_id_user_results_dict = community_id_user_results_instance.to_dict()
# create an instance of CommunityIdUserResults from a dict
community_id_user_results_from_dict = CommunityIdUserResults.from_dict(community_id_user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



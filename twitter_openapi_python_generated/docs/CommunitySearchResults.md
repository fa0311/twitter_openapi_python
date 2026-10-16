# CommunitySearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**CommunitySearchCommunity**](CommunitySearchCommunity.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_search_results import CommunitySearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySearchResults from a JSON string
community_search_results_instance = CommunitySearchResults.from_json(json)
# print the JSON string representation of the object
print(CommunitySearchResults.to_json())

# convert the object into a dict
community_search_results_dict = community_search_results_instance.to_dict()
# create an instance of CommunitySearchResults from a dict
community_search_results_from_dict = CommunitySearchResults.from_dict(community_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



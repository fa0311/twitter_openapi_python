# CommunityPageResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**CommunityPageCommunity**](CommunityPageCommunity.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_page_results import CommunityPageResults

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityPageResults from a JSON string
community_page_results_instance = CommunityPageResults.from_json(json)
# print the JSON string representation of the object
print(CommunityPageResults.to_json())

# convert the object into a dict
community_page_results_dict = community_page_results_instance.to_dict()
# create an instance of CommunityPageResults from a dict
community_page_results_from_dict = CommunityPageResults.from_dict(community_page_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



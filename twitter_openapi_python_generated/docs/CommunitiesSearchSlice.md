# CommunitiesSearchSlice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_results** | [**List[CommunitySearchResults]**](CommunitySearchResults.md) |  | 
**slice_info** | [**SliceInfo**](SliceInfo.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.communities_search_slice import CommunitiesSearchSlice

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitiesSearchSlice from a JSON string
communities_search_slice_instance = CommunitiesSearchSlice.from_json(json)
# print the JSON string representation of the object
print(CommunitiesSearchSlice.to_json())

# convert the object into a dict
communities_search_slice_dict = communities_search_slice_instance.to_dict()
# create an instance of CommunitiesSearchSlice from a dict
communities_search_slice_from_dict = CommunitiesSearchSlice.from_dict(communities_search_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommunityHashtagSlice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**items** | [**List[CommunityHashtag]**](CommunityHashtag.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_hashtag_slice import CommunityHashtagSlice

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityHashtagSlice from a JSON string
community_hashtag_slice_instance = CommunityHashtagSlice.from_json(json)
# print the JSON string representation of the object
print(CommunityHashtagSlice.to_json())

# convert the object into a dict
community_hashtag_slice_dict = community_hashtag_slice_instance.to_dict()
# create an instance of CommunityHashtagSlice from a dict
community_hashtag_slice_from_dict = CommunityHashtagSlice.from_dict(community_hashtag_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



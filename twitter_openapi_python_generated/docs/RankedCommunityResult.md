# RankedCommunityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**ranked_community_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.ranked_community_result import RankedCommunityResult

# TODO update the JSON string below
json = "{}"
# create an instance of RankedCommunityResult from a JSON string
ranked_community_result_instance = RankedCommunityResult.from_json(json)
# print the JSON string representation of the object
print(RankedCommunityResult.to_json())

# convert the object into a dict
ranked_community_result_dict = ranked_community_result_instance.to_dict()
# create an instance of RankedCommunityResult from a dict
ranked_community_result_from_dict = RankedCommunityResult.from_dict(ranked_community_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



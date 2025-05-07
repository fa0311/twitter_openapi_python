# RankedCommunityResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**RankedCommunityResult**](RankedCommunityResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.ranked_community_results import RankedCommunityResults

# TODO update the JSON string below
json = "{}"
# create an instance of RankedCommunityResults from a JSON string
ranked_community_results_instance = RankedCommunityResults.from_json(json)
# print the JSON string representation of the object
print(RankedCommunityResults.to_json())

# convert the object into a dict
ranked_community_results_dict = ranked_community_results_instance.to_dict()
# create an instance of RankedCommunityResults from a dict
ranked_community_results_from_dict = RankedCommunityResults.from_dict(ranked_community_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



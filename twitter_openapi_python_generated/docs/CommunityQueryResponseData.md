# CommunityQueryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_results** | [**CommunitySettingsResults**](CommunitySettingsResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_query_response_data import CommunityQueryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityQueryResponseData from a JSON string
community_query_response_data_instance = CommunityQueryResponseData.from_json(json)
# print the JSON string representation of the object
print(CommunityQueryResponseData.to_json())

# convert the object into a dict
community_query_response_data_dict = community_query_response_data_instance.to_dict()
# create an instance of CommunityQueryResponseData from a dict
community_query_response_data_from_dict = CommunityQueryResponseData.from_dict(community_query_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



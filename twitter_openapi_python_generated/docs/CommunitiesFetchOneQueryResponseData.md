# CommunitiesFetchOneQueryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_results** | [**CommunityPageResults**](CommunityPageResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.communities_fetch_one_query_response_data import CommunitiesFetchOneQueryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitiesFetchOneQueryResponseData from a JSON string
communities_fetch_one_query_response_data_instance = CommunitiesFetchOneQueryResponseData.from_json(json)
# print the JSON string representation of the object
print(CommunitiesFetchOneQueryResponseData.to_json())

# convert the object into a dict
communities_fetch_one_query_response_data_dict = communities_fetch_one_query_response_data_instance.to_dict()
# create an instance of CommunitiesFetchOneQueryResponseData from a dict
communities_fetch_one_query_response_data_from_dict = CommunitiesFetchOneQueryResponseData.from_dict(communities_fetch_one_query_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



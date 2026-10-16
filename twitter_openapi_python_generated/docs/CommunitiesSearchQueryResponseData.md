# CommunitiesSearchQueryResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communities_search_slice** | [**CommunitiesSearchSlice**](CommunitiesSearchSlice.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.communities_search_query_response_data import CommunitiesSearchQueryResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitiesSearchQueryResponseData from a JSON string
communities_search_query_response_data_instance = CommunitiesSearchQueryResponseData.from_json(json)
# print the JSON string representation of the object
print(CommunitiesSearchQueryResponseData.to_json())

# convert the object into a dict
communities_search_query_response_data_dict = communities_search_query_response_data_instance.to_dict()
# create an instance of CommunitiesSearchQueryResponseData from a dict
communities_search_query_response_data_from_dict = CommunitiesSearchQueryResponseData.from_dict(communities_search_query_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CommunitiesSearchQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunitiesSearchQueryResponseData**](CommunitiesSearchQueryResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.communities_search_query_response import CommunitiesSearchQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitiesSearchQueryResponse from a JSON string
communities_search_query_response_instance = CommunitiesSearchQueryResponse.from_json(json)
# print the JSON string representation of the object
print(CommunitiesSearchQueryResponse.to_json())

# convert the object into a dict
communities_search_query_response_dict = communities_search_query_response_instance.to_dict()
# create an instance of CommunitiesSearchQueryResponse from a dict
communities_search_query_response_from_dict = CommunitiesSearchQueryResponse.from_dict(communities_search_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



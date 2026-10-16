# CommunitiesFetchOneQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunitiesFetchOneQueryResponseData**](CommunitiesFetchOneQueryResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.communities_fetch_one_query_response import CommunitiesFetchOneQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitiesFetchOneQueryResponse from a JSON string
communities_fetch_one_query_response_instance = CommunitiesFetchOneQueryResponse.from_json(json)
# print the JSON string representation of the object
print(CommunitiesFetchOneQueryResponse.to_json())

# convert the object into a dict
communities_fetch_one_query_response_dict = communities_fetch_one_query_response_instance.to_dict()
# create an instance of CommunitiesFetchOneQueryResponse from a dict
communities_fetch_one_query_response_from_dict = CommunitiesFetchOneQueryResponse.from_dict(communities_fetch_one_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



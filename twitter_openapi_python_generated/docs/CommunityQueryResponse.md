# CommunityQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CommunityQueryResponseData**](CommunityQueryResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.community_query_response import CommunityQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityQueryResponse from a JSON string
community_query_response_instance = CommunityQueryResponse.from_json(json)
# print the JSON string representation of the object
print(CommunityQueryResponse.to_json())

# convert the object into a dict
community_query_response_dict = community_query_response_instance.to_dict()
# create an instance of CommunityQueryResponse from a dict
community_query_response_from_dict = CommunityQueryResponse.from_dict(community_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListRecommendedUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListRecommendedUsersResponseData**](ListRecommendedUsersResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.list_recommended_users_response import ListRecommendedUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecommendedUsersResponse from a JSON string
list_recommended_users_response_instance = ListRecommendedUsersResponse.from_json(json)
# print the JSON string representation of the object
print(ListRecommendedUsersResponse.to_json())

# convert the object into a dict
list_recommended_users_response_dict = list_recommended_users_response_instance.to_dict()
# create an instance of ListRecommendedUsersResponse from a dict
list_recommended_users_response_from_dict = ListRecommendedUsersResponse.from_dict(list_recommended_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



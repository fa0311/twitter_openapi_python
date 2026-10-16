# ListRecommendedUsersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ListRecommendedUsersList**](ListRecommendedUsersList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_recommended_users_response_data import ListRecommendedUsersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecommendedUsersResponseData from a JSON string
list_recommended_users_response_data_instance = ListRecommendedUsersResponseData.from_json(json)
# print the JSON string representation of the object
print(ListRecommendedUsersResponseData.to_json())

# convert the object into a dict
list_recommended_users_response_data_dict = list_recommended_users_response_data_instance.to_dict()
# create an instance of ListRecommendedUsersResponseData from a dict
list_recommended_users_response_data_from_dict = ListRecommendedUsersResponseData.from_dict(list_recommended_users_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



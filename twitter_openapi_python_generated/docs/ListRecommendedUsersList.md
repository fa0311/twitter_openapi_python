# ListRecommendedUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommended_users** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_recommended_users_list import ListRecommendedUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecommendedUsersList from a JSON string
list_recommended_users_list_instance = ListRecommendedUsersList.from_json(json)
# print the JSON string representation of the object
print(ListRecommendedUsersList.to_json())

# convert the object into a dict
list_recommended_users_list_dict = list_recommended_users_list_instance.to_dict()
# create an instance of ListRecommendedUsersList from a dict
list_recommended_users_list_from_dict = ListRecommendedUsersList.from_dict(list_recommended_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreatorStudioTabBarItemQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreatorStudioTabBarItemQueryResponseData**](CreatorStudioTabBarItemQueryResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.creator_studio_tab_bar_item_query_response import CreatorStudioTabBarItemQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorStudioTabBarItemQueryResponse from a JSON string
creator_studio_tab_bar_item_query_response_instance = CreatorStudioTabBarItemQueryResponse.from_json(json)
# print the JSON string representation of the object
print(CreatorStudioTabBarItemQueryResponse.to_json())

# convert the object into a dict
creator_studio_tab_bar_item_query_response_dict = creator_studio_tab_bar_item_query_response_instance.to_dict()
# create an instance of CreatorStudioTabBarItemQueryResponse from a dict
creator_studio_tab_bar_item_query_response_from_dict = CreatorStudioTabBarItemQueryResponse.from_dict(creator_studio_tab_bar_item_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



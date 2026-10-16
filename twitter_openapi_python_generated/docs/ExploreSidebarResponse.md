# ExploreSidebarResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExploreSidebarResponseData**](ExploreSidebarResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.explore_sidebar_response import ExploreSidebarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreSidebarResponse from a JSON string
explore_sidebar_response_instance = ExploreSidebarResponse.from_json(json)
# print the JSON string representation of the object
print(ExploreSidebarResponse.to_json())

# convert the object into a dict
explore_sidebar_response_dict = explore_sidebar_response_instance.to_dict()
# create an instance of ExploreSidebarResponse from a dict
explore_sidebar_response_from_dict = ExploreSidebarResponse.from_dict(explore_sidebar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



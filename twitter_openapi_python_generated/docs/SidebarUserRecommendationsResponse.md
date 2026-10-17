# SidebarUserRecommendationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SidebarUserRecommendationsData**](SidebarUserRecommendationsData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.sidebar_user_recommendations_response import SidebarUserRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SidebarUserRecommendationsResponse from a JSON string
sidebar_user_recommendations_response_instance = SidebarUserRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(SidebarUserRecommendationsResponse.to_json())

# convert the object into a dict
sidebar_user_recommendations_response_dict = sidebar_user_recommendations_response_instance.to_dict()
# create an instance of SidebarUserRecommendationsResponse from a dict
sidebar_user_recommendations_response_from_dict = SidebarUserRecommendationsResponse.from_dict(sidebar_user_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



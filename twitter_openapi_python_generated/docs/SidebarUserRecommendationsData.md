# SidebarUserRecommendationsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sidebar_user_recommendations** | [**List[SidebarUserRecommendation]**](SidebarUserRecommendation.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.sidebar_user_recommendations_data import SidebarUserRecommendationsData

# TODO update the JSON string below
json = "{}"
# create an instance of SidebarUserRecommendationsData from a JSON string
sidebar_user_recommendations_data_instance = SidebarUserRecommendationsData.from_json(json)
# print the JSON string representation of the object
print(SidebarUserRecommendationsData.to_json())

# convert the object into a dict
sidebar_user_recommendations_data_dict = sidebar_user_recommendations_data_instance.to_dict()
# create an instance of SidebarUserRecommendationsData from a dict
sidebar_user_recommendations_data_from_dict = SidebarUserRecommendationsData.from_dict(sidebar_user_recommendations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



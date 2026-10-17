# SidebarUserRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**user_results** | [**UserResults**](UserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.sidebar_user_recommendation import SidebarUserRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SidebarUserRecommendation from a JSON string
sidebar_user_recommendation_instance = SidebarUserRecommendation.from_json(json)
# print the JSON string representation of the object
print(SidebarUserRecommendation.to_json())

# convert the object into a dict
sidebar_user_recommendation_dict = sidebar_user_recommendation_instance.to_dict()
# create an instance of SidebarUserRecommendation from a dict
sidebar_user_recommendation_from_dict = SidebarUserRecommendation.from_dict(sidebar_user_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



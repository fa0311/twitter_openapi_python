# ExplorePageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explore_page** | [**ExplorePage**](ExplorePage.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.explore_page_response_data import ExplorePageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorePageResponseData from a JSON string
explore_page_response_data_instance = ExplorePageResponseData.from_json(json)
# print the JSON string representation of the object
print(ExplorePageResponseData.to_json())

# convert the object into a dict
explore_page_response_data_dict = explore_page_response_data_instance.to_dict()
# create an instance of ExplorePageResponseData from a dict
explore_page_response_data_from_dict = ExplorePageResponseData.from_dict(explore_page_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



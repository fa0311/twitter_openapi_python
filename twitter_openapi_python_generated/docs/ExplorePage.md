# ExplorePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**ExplorePageBody**](ExplorePageBody.md) |  | 
**id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.explore_page import ExplorePage

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorePage from a JSON string
explore_page_instance = ExplorePage.from_json(json)
# print the JSON string representation of the object
print(ExplorePage.to_json())

# convert the object into a dict
explore_page_dict = explore_page_instance.to_dict()
# create an instance of ExplorePage from a dict
explore_page_from_dict = ExplorePage.from_dict(explore_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



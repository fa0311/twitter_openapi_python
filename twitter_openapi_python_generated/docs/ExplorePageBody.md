# ExplorePageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**initial_timeline** | [**ExploreTimeline**](ExploreTimeline.md) |  | 
**timelines** | [**List[ExploreTimeline]**](ExploreTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.explore_page_body import ExplorePageBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorePageBody from a JSON string
explore_page_body_instance = ExplorePageBody.from_json(json)
# print the JSON string representation of the object
print(ExplorePageBody.to_json())

# convert the object into a dict
explore_page_body_dict = explore_page_body_instance.to_dict()
# create an instance of ExplorePageBody from a dict
explore_page_body_from_dict = ExplorePageBody.from_dict(explore_page_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



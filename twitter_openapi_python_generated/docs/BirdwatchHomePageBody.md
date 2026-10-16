# BirdwatchHomePageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**initial_timeline** | [**BirdwatchHomeTimeline**](BirdwatchHomeTimeline.md) |  | 
**timelines** | [**List[BirdwatchHomeTimeline]**](BirdwatchHomeTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_home_page_body import BirdwatchHomePageBody

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchHomePageBody from a JSON string
birdwatch_home_page_body_instance = BirdwatchHomePageBody.from_json(json)
# print the JSON string representation of the object
print(BirdwatchHomePageBody.to_json())

# convert the object into a dict
birdwatch_home_page_body_dict = birdwatch_home_page_body_instance.to_dict()
# create an instance of BirdwatchHomePageBody from a dict
birdwatch_home_page_body_from_dict = BirdwatchHomePageBody.from_dict(birdwatch_home_page_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



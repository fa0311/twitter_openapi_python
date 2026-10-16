# BirdwatchHomeTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label_text** | **str** |  | 
**timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_home_timeline import BirdwatchHomeTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchHomeTimeline from a JSON string
birdwatch_home_timeline_instance = BirdwatchHomeTimeline.from_json(json)
# print the JSON string representation of the object
print(BirdwatchHomeTimeline.to_json())

# convert the object into a dict
birdwatch_home_timeline_dict = birdwatch_home_timeline_instance.to_dict()
# create an instance of BirdwatchHomeTimeline from a dict
birdwatch_home_timeline_from_dict = BirdwatchHomeTimeline.from_dict(birdwatch_home_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



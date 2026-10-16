# ExploreTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label_text** | **str** |  | 
**refresh_interval_sec** | **int** |  | 
**scribe_config** | [**ExploreTimelineScribeConfig**](ExploreTimelineScribeConfig.md) |  | 
**timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.explore_timeline import ExploreTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreTimeline from a JSON string
explore_timeline_instance = ExploreTimeline.from_json(json)
# print the JSON string representation of the object
print(ExploreTimeline.to_json())

# convert the object into a dict
explore_timeline_dict = explore_timeline_instance.to_dict()
# create an instance of ExploreTimeline from a dict
explore_timeline_from_dict = ExploreTimeline.from_dict(explore_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



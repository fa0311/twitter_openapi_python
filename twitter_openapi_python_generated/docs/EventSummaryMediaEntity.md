# EventSummaryMediaEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet_results** | [**ItemResult**](ItemResult.md) |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.event_summary_media_entity import EventSummaryMediaEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EventSummaryMediaEntity from a JSON string
event_summary_media_entity_instance = EventSummaryMediaEntity.from_json(json)
# print the JSON string representation of the object
print(EventSummaryMediaEntity.to_json())

# convert the object into a dict
event_summary_media_entity_dict = event_summary_media_entity_instance.to_dict()
# create an instance of EventSummaryMediaEntity from a dict
event_summary_media_entity_from_dict = EventSummaryMediaEntity.from_dict(event_summary_media_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



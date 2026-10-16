# TimelineEventSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**event** | [**EventSummaryEvent**](EventSummaryEvent.md) |  | 
**event_summary_display_type** | **str** |  | 
**event_summary_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**media** | [**EventSummaryMedia**](EventSummaryMedia.md) |  | 
**promoted_metadata** | [**EventSummaryPromotedMetadata**](EventSummaryPromotedMetadata.md) |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_event_summary import TimelineEventSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineEventSummary from a JSON string
timeline_event_summary_instance = TimelineEventSummary.from_json(json)
# print the JSON string representation of the object
print(TimelineEventSummary.to_json())

# convert the object into a dict
timeline_event_summary_dict = timeline_event_summary_instance.to_dict()
# create an instance of TimelineEventSummary from a dict
timeline_event_summary_from_dict = TimelineEventSummary.from_dict(timeline_event_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



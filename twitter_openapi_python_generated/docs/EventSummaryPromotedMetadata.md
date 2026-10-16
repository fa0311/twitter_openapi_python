# EventSummaryPromotedMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_metadata_container** | [**EventSummaryAdMetadataContainer**](EventSummaryAdMetadataContainer.md) |  | 
**advertiser_results** | [**UserResults**](UserResults.md) |  | 
**disclosure_type** | **str** |  | 
**impression_id** | **str** |  | 
**impression_string** | **str** |  | 
**promoted_trend** | [**PromotedTrend**](PromotedTrend.md) |  | 
**promoted_trend_description** | **str** |  | 
**promoted_trend_name** | **str** |  | 
**promoted_trend_query_term** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.event_summary_promoted_metadata import EventSummaryPromotedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EventSummaryPromotedMetadata from a JSON string
event_summary_promoted_metadata_instance = EventSummaryPromotedMetadata.from_json(json)
# print the JSON string representation of the object
print(EventSummaryPromotedMetadata.to_json())

# convert the object into a dict
event_summary_promoted_metadata_dict = event_summary_promoted_metadata_instance.to_dict()
# create an instance of EventSummaryPromotedMetadata from a dict
event_summary_promoted_metadata_from_dict = EventSummaryPromotedMetadata.from_dict(event_summary_promoted_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



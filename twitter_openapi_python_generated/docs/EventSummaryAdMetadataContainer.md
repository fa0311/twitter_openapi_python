# EventSummaryAdMetadataContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_quick_promote** | **bool** |  | 
**render_sales_cta_website_card** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.event_summary_ad_metadata_container import EventSummaryAdMetadataContainer

# TODO update the JSON string below
json = "{}"
# create an instance of EventSummaryAdMetadataContainer from a JSON string
event_summary_ad_metadata_container_instance = EventSummaryAdMetadataContainer.from_json(json)
# print the JSON string representation of the object
print(EventSummaryAdMetadataContainer.to_json())

# convert the object into a dict
event_summary_ad_metadata_container_dict = event_summary_ad_metadata_container_instance.to_dict()
# create an instance of EventSummaryAdMetadataContainer from a dict
event_summary_ad_metadata_container_from_dict = EventSummaryAdMetadataContainer.from_dict(event_summary_ad_metadata_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



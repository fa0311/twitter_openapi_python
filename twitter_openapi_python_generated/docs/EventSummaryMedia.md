# EventSummaryMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_entity** | [**EventSummaryMediaEntity**](EventSummaryMediaEntity.md) |  | 
**media_key** | [**EventSummaryMediaKey**](EventSummaryMediaKey.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.event_summary_media import EventSummaryMedia

# TODO update the JSON string below
json = "{}"
# create an instance of EventSummaryMedia from a JSON string
event_summary_media_instance = EventSummaryMedia.from_json(json)
# print the JSON string representation of the object
print(EventSummaryMedia.to_json())

# convert the object into a dict
event_summary_media_dict = event_summary_media_instance.to_dict()
# create an instance of EventSummaryMedia from a dict
event_summary_media_from_dict = EventSummaryMedia.from_dict(event_summary_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



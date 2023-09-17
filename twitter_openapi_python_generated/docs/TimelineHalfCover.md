# TimelineHalfCover


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dismissible** | **bool** |  | 
**half_cover_display_type** | **str** |  | 
**impression_callbacks** | [**List[Callback]**](Callback.md) |  | 
**primary_cover_cta** | [**CoverCta**](CoverCta.md) |  | 
**primary_text** | [**Text**](Text.md) |  | 
**secondary_text** | [**Text**](Text.md) |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_half_cover import TimelineHalfCover

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineHalfCover from a JSON string
timeline_half_cover_instance = TimelineHalfCover.from_json(json)
# print the JSON string representation of the object
print TimelineHalfCover.to_json()

# convert the object into a dict
timeline_half_cover_dict = timeline_half_cover_instance.to_dict()
# create an instance of TimelineHalfCover from a dict
timeline_half_cover_form_dict = timeline_half_cover.from_dict(timeline_half_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



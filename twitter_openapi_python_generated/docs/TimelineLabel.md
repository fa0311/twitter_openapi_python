# TimelineLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**text** | **str** |  | 
**url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_label import TimelineLabel

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineLabel from a JSON string
timeline_label_instance = TimelineLabel.from_json(json)
# print the JSON string representation of the object
print(TimelineLabel.to_json())

# convert the object into a dict
timeline_label_dict = timeline_label_instance.to_dict()
# create an instance of TimelineLabel from a dict
timeline_label_from_dict = TimelineLabel.from_dict(timeline_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



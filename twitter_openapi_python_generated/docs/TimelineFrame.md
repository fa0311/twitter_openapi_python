# TimelineFrame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**height** | **int** |  | 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**payload** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_frame import TimelineFrame

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineFrame from a JSON string
timeline_frame_instance = TimelineFrame.from_json(json)
# print the JSON string representation of the object
print(TimelineFrame.to_json())

# convert the object into a dict
timeline_frame_dict = timeline_frame_instance.to_dict()
# create an instance of TimelineFrame from a dict
timeline_frame_from_dict = TimelineFrame.from_dict(timeline_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimelineTwitterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**display_type** | **str** |  | [optional] 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | 
**list** | [**TwitterList**](TwitterList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_twitter_list import TimelineTwitterList

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTwitterList from a JSON string
timeline_twitter_list_instance = TimelineTwitterList.from_json(json)
# print the JSON string representation of the object
print(TimelineTwitterList.to_json())

# convert the object into a dict
timeline_twitter_list_dict = timeline_twitter_list_instance.to_dict()
# create an instance of TimelineTwitterList from a dict
timeline_twitter_list_from_dict = TimelineTwitterList.from_dict(timeline_twitter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimelineTombstone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | [optional] 
**tombstone_display_type** | **str** |  | [optional] 
**tombstone_info** | [**TombstoneInfo**](TombstoneInfo.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.timeline_tombstone import TimelineTombstone

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTombstone from a JSON string
timeline_tombstone_instance = TimelineTombstone.from_json(json)
# print the JSON string representation of the object
print(TimelineTombstone.to_json())

# convert the object into a dict
timeline_tombstone_dict = timeline_tombstone_instance.to_dict()
# create an instance of TimelineTombstone from a dict
timeline_tombstone_from_dict = TimelineTombstone.from_dict(timeline_tombstone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TimelineMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reader_mode_config** | [**ReaderModeConfig**](ReaderModeConfig.md) |  | [optional] 
**scribe_config** | [**ScribeConfig**](ScribeConfig.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_metadata import TimelineMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineMetadata from a JSON string
timeline_metadata_instance = TimelineMetadata.from_json(json)
# print the JSON string representation of the object
print(TimelineMetadata.to_json())

# convert the object into a dict
timeline_metadata_dict = timeline_metadata_instance.to_dict()
# create an instance of TimelineMetadata from a dict
timeline_metadata_from_dict = TimelineMetadata.from_dict(timeline_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



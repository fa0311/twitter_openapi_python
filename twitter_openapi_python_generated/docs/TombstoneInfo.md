# TombstoneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rich_text** | [**TombstoneRichText**](TombstoneRichText.md) |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tombstone_info import TombstoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TombstoneInfo from a JSON string
tombstone_info_instance = TombstoneInfo.from_json(json)
# print the JSON string representation of the object
print(TombstoneInfo.to_json())

# convert the object into a dict
tombstone_info_dict = tombstone_info_instance.to_dict()
# create an instance of TombstoneInfo from a dict
tombstone_info_from_dict = TombstoneInfo.from_dict(tombstone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



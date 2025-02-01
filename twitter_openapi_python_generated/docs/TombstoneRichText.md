# TombstoneRichText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[TombstoneEntity]**](TombstoneEntity.md) |  | [optional] 
**rtl** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.tombstone_rich_text import TombstoneRichText

# TODO update the JSON string below
json = "{}"
# create an instance of TombstoneRichText from a JSON string
tombstone_rich_text_instance = TombstoneRichText.from_json(json)
# print the JSON string representation of the object
print(TombstoneRichText.to_json())

# convert the object into a dict
tombstone_rich_text_dict = tombstone_rich_text_instance.to_dict()
# create an instance of TombstoneRichText from a dict
tombstone_rich_text_from_dict = TombstoneRichText.from_dict(tombstone_rich_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



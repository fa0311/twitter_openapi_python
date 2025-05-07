# RichMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rtl** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.rich_message import RichMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RichMessage from a JSON string
rich_message_instance = RichMessage.from_json(json)
# print the JSON string representation of the object
print(RichMessage.to_json())

# convert the object into a dict
rich_message_dict = rich_message_instance.to_dict()
# create an instance of RichMessage from a dict
rich_message_from_dict = RichMessage.from_dict(rich_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



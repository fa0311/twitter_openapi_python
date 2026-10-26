# RichMessageEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**from_index** | **int** |  | 
**ref** | [**RichMessageEntityRef**](RichMessageEntityRef.md) |  | [optional] 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.rich_message_entity import RichMessageEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RichMessageEntity from a JSON string
rich_message_entity_instance = RichMessageEntity.from_json(json)
# print the JSON string representation of the object
print(RichMessageEntity.to_json())

# convert the object into a dict
rich_message_entity_dict = rich_message_entity_instance.to_dict()
# create an instance of RichMessageEntity from a dict
rich_message_entity_from_dict = RichMessageEntity.from_dict(rich_message_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



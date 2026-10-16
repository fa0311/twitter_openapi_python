# RichMessageEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | [optional] 
**user_results** | [**UserResults**](UserResults.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.rich_message_entity_ref import RichMessageEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of RichMessageEntityRef from a JSON string
rich_message_entity_ref_instance = RichMessageEntityRef.from_json(json)
# print the JSON string representation of the object
print(RichMessageEntityRef.to_json())

# convert the object into a dict
rich_message_entity_ref_dict = rich_message_entity_ref_instance.to_dict()
# create an instance of RichMessageEntityRef from a dict
rich_message_entity_ref_from_dict = RichMessageEntityRef.from_dict(rich_message_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModuleMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_metadata** | [**ConversationMetadata**](ConversationMetadata.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.module_metadata import ModuleMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleMetadata from a JSON string
module_metadata_instance = ModuleMetadata.from_json(json)
# print the JSON string representation of the object
print(ModuleMetadata.to_json())

# convert the object into a dict
module_metadata_dict = module_metadata_instance.to_dict()
# create an instance of ModuleMetadata from a dict
module_metadata_from_dict = ModuleMetadata.from_dict(module_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConversationOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**core** | [**ConversationOwnerCore**](ConversationOwnerCore.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.conversation_owner import ConversationOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationOwner from a JSON string
conversation_owner_instance = ConversationOwner.from_json(json)
# print the JSON string representation of the object
print(ConversationOwner.to_json())

# convert the object into a dict
conversation_owner_dict = conversation_owner_instance.to_dict()
# create an instance of ConversationOwner from a dict
conversation_owner_from_dict = ConversationOwner.from_dict(conversation_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



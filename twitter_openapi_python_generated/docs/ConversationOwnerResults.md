# ConversationOwnerResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ConversationOwner**](ConversationOwner.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.conversation_owner_results import ConversationOwnerResults

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationOwnerResults from a JSON string
conversation_owner_results_instance = ConversationOwnerResults.from_json(json)
# print the JSON string representation of the object
print(ConversationOwnerResults.to_json())

# convert the object into a dict
conversation_owner_results_dict = conversation_owner_results_instance.to_dict()
# create an instance of ConversationOwnerResults from a dict
conversation_owner_results_from_dict = ConversationOwnerResults.from_dict(conversation_owner_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



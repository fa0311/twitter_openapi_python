# ConversationMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tweet_ids** | **List[str]** |  | 
**enable_deduplication** | **bool** |  | 

## Example

```python
from twitter_openapi_python_generated.models.conversation_metadata import ConversationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMetadata from a JSON string
conversation_metadata_instance = ConversationMetadata.from_json(json)
# print the JSON string representation of the object
print(ConversationMetadata.to_json())

# convert the object into a dict
conversation_metadata_dict = conversation_metadata_instance.to_dict()
# create an instance of ConversationMetadata from a dict
conversation_metadata_from_dict = ConversationMetadata.from_dict(conversation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



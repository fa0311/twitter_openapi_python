# DeleteDraftTweetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteDraftTweetsResponseData**](DeleteDraftTweetsResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_draft_tweets_response import DeleteDraftTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDraftTweetsResponse from a JSON string
delete_draft_tweets_response_instance = DeleteDraftTweetsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteDraftTweetsResponse.to_json())

# convert the object into a dict
delete_draft_tweets_response_dict = delete_draft_tweets_response_instance.to_dict()
# create an instance of DeleteDraftTweetsResponse from a dict
delete_draft_tweets_response_from_dict = DeleteDraftTweetsResponse.from_dict(delete_draft_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



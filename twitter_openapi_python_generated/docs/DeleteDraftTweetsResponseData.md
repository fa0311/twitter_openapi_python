# DeleteDraftTweetsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_tweets_batch_delete** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.delete_draft_tweets_response_data import DeleteDraftTweetsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDraftTweetsResponseData from a JSON string
delete_draft_tweets_response_data_instance = DeleteDraftTweetsResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteDraftTweetsResponseData.to_json())

# convert the object into a dict
delete_draft_tweets_response_data_dict = delete_draft_tweets_response_data_instance.to_dict()
# create an instance of DeleteDraftTweetsResponseData from a dict
delete_draft_tweets_response_data_from_dict = DeleteDraftTweetsResponseData.from_dict(delete_draft_tweets_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



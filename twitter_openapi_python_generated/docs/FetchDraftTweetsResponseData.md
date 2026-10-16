# FetchDraftTweetsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**viewer** | [**DraftTweetsViewer**](DraftTweetsViewer.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.fetch_draft_tweets_response_data import FetchDraftTweetsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDraftTweetsResponseData from a JSON string
fetch_draft_tweets_response_data_instance = FetchDraftTweetsResponseData.from_json(json)
# print the JSON string representation of the object
print(FetchDraftTweetsResponseData.to_json())

# convert the object into a dict
fetch_draft_tweets_response_data_dict = fetch_draft_tweets_response_data_instance.to_dict()
# create an instance of FetchDraftTweetsResponseData from a dict
fetch_draft_tweets_response_data_from_dict = FetchDraftTweetsResponseData.from_dict(fetch_draft_tweets_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



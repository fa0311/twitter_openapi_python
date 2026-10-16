# FetchDraftTweetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FetchDraftTweetsResponseData**](FetchDraftTweetsResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.fetch_draft_tweets_response import FetchDraftTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDraftTweetsResponse from a JSON string
fetch_draft_tweets_response_instance = FetchDraftTweetsResponse.from_json(json)
# print the JSON string representation of the object
print(FetchDraftTweetsResponse.to_json())

# convert the object into a dict
fetch_draft_tweets_response_dict = fetch_draft_tweets_response_instance.to_dict()
# create an instance of FetchDraftTweetsResponse from a dict
fetch_draft_tweets_response_from_dict = FetchDraftTweetsResponse.from_dict(fetch_draft_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



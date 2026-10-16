# CreateDraftTweetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateDraftTweetResponseData**](CreateDraftTweetResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.create_draft_tweet_response import CreateDraftTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDraftTweetResponse from a JSON string
create_draft_tweet_response_instance = CreateDraftTweetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDraftTweetResponse.to_json())

# convert the object into a dict
create_draft_tweet_response_dict = create_draft_tweet_response_instance.to_dict()
# create an instance of CreateDraftTweetResponse from a dict
create_draft_tweet_response_from_dict = CreateDraftTweetResponse.from_dict(create_draft_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



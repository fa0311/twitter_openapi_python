# CreateDraftTweetResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tweet** | [**CreateDraftTweetResponseTweet**](CreateDraftTweetResponseTweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_draft_tweet_response_data import CreateDraftTweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDraftTweetResponseData from a JSON string
create_draft_tweet_response_data_instance = CreateDraftTweetResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateDraftTweetResponseData.to_json())

# convert the object into a dict
create_draft_tweet_response_data_dict = create_draft_tweet_response_data_instance.to_dict()
# create an instance of CreateDraftTweetResponseData from a dict
create_draft_tweet_response_data_from_dict = CreateDraftTweetResponseData.from_dict(create_draft_tweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



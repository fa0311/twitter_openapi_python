# DraftTweetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_populate_reply_metadata** | **bool** |  | 
**exclude_reply_user_ids** | **List[str]** |  | 
**media_ids** | **List[str]** |  | 
**status** | **str** |  | 
**thread_tweets** | **List[Dict[str, object]]** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.draft_tweet_create_request import DraftTweetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTweetCreateRequest from a JSON string
draft_tweet_create_request_instance = DraftTweetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DraftTweetCreateRequest.to_json())

# convert the object into a dict
draft_tweet_create_request_dict = draft_tweet_create_request_instance.to_dict()
# create an instance of DraftTweetCreateRequest from a dict
draft_tweet_create_request_from_dict = DraftTweetCreateRequest.from_dict(draft_tweet_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



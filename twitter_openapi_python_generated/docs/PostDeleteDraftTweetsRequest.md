# PostDeleteDraftTweetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | [default to 'h0rzaIYc9-v3zTQvx1J8OA']
**variables** | [**PostDeleteDraftTweetsRequestVariables**](PostDeleteDraftTweetsRequestVariables.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_draft_tweets_request import PostDeleteDraftTweetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteDraftTweetsRequest from a JSON string
post_delete_draft_tweets_request_instance = PostDeleteDraftTweetsRequest.from_json(json)
# print the JSON string representation of the object
print(PostDeleteDraftTweetsRequest.to_json())

# convert the object into a dict
post_delete_draft_tweets_request_dict = post_delete_draft_tweets_request_instance.to_dict()
# create an instance of PostDeleteDraftTweetsRequest from a dict
post_delete_draft_tweets_request_from_dict = PostDeleteDraftTweetsRequest.from_dict(post_delete_draft_tweets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



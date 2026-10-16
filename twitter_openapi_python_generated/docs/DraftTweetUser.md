# DraftTweetUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.draft_tweet_user import DraftTweetUser

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTweetUser from a JSON string
draft_tweet_user_instance = DraftTweetUser.from_json(json)
# print the JSON string representation of the object
print(DraftTweetUser.to_json())

# convert the object into a dict
draft_tweet_user_dict = draft_tweet_user_instance.to_dict()
# create an instance of DraftTweetUser from a dict
draft_tweet_user_from_dict = DraftTweetUser.from_dict(draft_tweet_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



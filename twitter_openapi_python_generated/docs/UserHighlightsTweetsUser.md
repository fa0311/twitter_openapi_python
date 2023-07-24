# UserHighlightsTweetsUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**UserHighlightsTweetsResult**](UserHighlightsTweetsResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_tweets_user import UserHighlightsTweetsUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsTweetsUser from a JSON string
user_highlights_tweets_user_instance = UserHighlightsTweetsUser.from_json(json)
# print the JSON string representation of the object
print UserHighlightsTweetsUser.to_json()

# convert the object into a dict
user_highlights_tweets_user_dict = user_highlights_tweets_user_instance.to_dict()
# create an instance of UserHighlightsTweetsUser from a dict
user_highlights_tweets_user_form_dict = user_highlights_tweets_user.from_dict(user_highlights_tweets_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



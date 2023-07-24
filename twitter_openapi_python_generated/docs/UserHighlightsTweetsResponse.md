# UserHighlightsTweetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserHighlightsTweetsData**](UserHighlightsTweetsData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_tweets_response import UserHighlightsTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsTweetsResponse from a JSON string
user_highlights_tweets_response_instance = UserHighlightsTweetsResponse.from_json(json)
# print the JSON string representation of the object
print UserHighlightsTweetsResponse.to_json()

# convert the object into a dict
user_highlights_tweets_response_dict = user_highlights_tweets_response_instance.to_dict()
# create an instance of UserHighlightsTweetsResponse from a dict
user_highlights_tweets_response_form_dict = user_highlights_tweets_response.from_dict(user_highlights_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



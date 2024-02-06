# UserHighlightsTweetsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**timeline** | [**UserHighlightsTweetsTimeline**](UserHighlightsTweetsTimeline.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_tweets_result import UserHighlightsTweetsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsTweetsResult from a JSON string
user_highlights_tweets_result_instance = UserHighlightsTweetsResult.from_json(json)
# print the JSON string representation of the object
print UserHighlightsTweetsResult.to_json()

# convert the object into a dict
user_highlights_tweets_result_dict = user_highlights_tweets_result_instance.to_dict()
# create an instance of UserHighlightsTweetsResult from a dict
user_highlights_tweets_result_form_dict = user_highlights_tweets_result.from_dict(user_highlights_tweets_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



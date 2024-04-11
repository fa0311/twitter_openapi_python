# UserHighlightsTweetsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserHighlightsTweetsUser**](UserHighlightsTweetsUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_highlights_tweets_data import UserHighlightsTweetsData

# TODO update the JSON string below
json = "{}"
# create an instance of UserHighlightsTweetsData from a JSON string
user_highlights_tweets_data_instance = UserHighlightsTweetsData.from_json(json)
# print the JSON string representation of the object
print(UserHighlightsTweetsData.to_json())

# convert the object into a dict
user_highlights_tweets_data_dict = user_highlights_tweets_data_instance.to_dict()
# create an instance of UserHighlightsTweetsData from a dict
user_highlights_tweets_data_form_dict = user_highlights_tweets_data.from_dict(user_highlights_tweets_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



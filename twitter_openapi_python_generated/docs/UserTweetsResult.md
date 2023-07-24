# UserTweetsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**timeline_v2** | [**TimelineV2**](TimelineV2.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_result import UserTweetsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsResult from a JSON string
user_tweets_result_instance = UserTweetsResult.from_json(json)
# print the JSON string representation of the object
print UserTweetsResult.to_json()

# convert the object into a dict
user_tweets_result_dict = user_tweets_result_instance.to_dict()
# create an instance of UserTweetsResult from a dict
user_tweets_result_form_dict = user_tweets_result.from_dict(user_tweets_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



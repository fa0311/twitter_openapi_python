# UserTweetsResultV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**timeline_v2** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_result_v2 import UserTweetsResultV2

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsResultV2 from a JSON string
user_tweets_result_v2_instance = UserTweetsResultV2.from_json(json)
# print the JSON string representation of the object
print(UserTweetsResultV2.to_json())

# convert the object into a dict
user_tweets_result_v2_dict = user_tweets_result_v2_instance.to_dict()
# create an instance of UserTweetsResultV2 from a dict
user_tweets_result_v2_from_dict = UserTweetsResultV2.from_dict(user_tweets_result_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



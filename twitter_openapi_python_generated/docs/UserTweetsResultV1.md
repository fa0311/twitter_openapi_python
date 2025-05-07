# UserTweetsResultV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_result_v1 import UserTweetsResultV1

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsResultV1 from a JSON string
user_tweets_result_v1_instance = UserTweetsResultV1.from_json(json)
# print the JSON string representation of the object
print(UserTweetsResultV1.to_json())

# convert the object into a dict
user_tweets_result_v1_dict = user_tweets_result_v1_instance.to_dict()
# create an instance of UserTweetsResultV1 from a dict
user_tweets_result_v1_from_dict = UserTweetsResultV1.from_dict(user_tweets_result_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



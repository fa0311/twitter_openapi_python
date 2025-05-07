# UserTweetsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**UserTweetsResultV1**](UserTweetsResultV1.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_user import UserTweetsUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsUser from a JSON string
user_tweets_user_instance = UserTweetsUser.from_json(json)
# print the JSON string representation of the object
print(UserTweetsUser.to_json())

# convert the object into a dict
user_tweets_user_dict = user_tweets_user_instance.to_dict()
# create an instance of UserTweetsUser from a dict
user_tweets_user_from_dict = UserTweetsUser.from_dict(user_tweets_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



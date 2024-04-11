# UserTweetsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserTweetsUser**](UserTweetsUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_data import UserTweetsData

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsData from a JSON string
user_tweets_data_instance = UserTweetsData.from_json(json)
# print the JSON string representation of the object
print(UserTweetsData.to_json())

# convert the object into a dict
user_tweets_data_dict = user_tweets_data_instance.to_dict()
# create an instance of UserTweetsData from a dict
user_tweets_data_form_dict = user_tweets_data.from_dict(user_tweets_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



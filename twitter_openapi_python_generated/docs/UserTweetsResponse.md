# UserTweetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserTweetsData**](UserTweetsData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_tweets_response import UserTweetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTweetsResponse from a JSON string
user_tweets_response_instance = UserTweetsResponse.from_json(json)
# print the JSON string representation of the object
print(UserTweetsResponse.to_json())

# convert the object into a dict
user_tweets_response_dict = user_tweets_response_instance.to_dict()
# create an instance of UserTweetsResponse from a dict
user_tweets_response_from_dict = UserTweetsResponse.from_dict(user_tweets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



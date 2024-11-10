# DeleteTweetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteTweetResponseData**](DeleteTweetResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_tweet_response import DeleteTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTweetResponse from a JSON string
delete_tweet_response_instance = DeleteTweetResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteTweetResponse.to_json())

# convert the object into a dict
delete_tweet_response_dict = delete_tweet_response_instance.to_dict()
# create an instance of DeleteTweetResponse from a dict
delete_tweet_response_from_dict = DeleteTweetResponse.from_dict(delete_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



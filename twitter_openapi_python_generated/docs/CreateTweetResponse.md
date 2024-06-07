# CreateTweetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTweetResponseData**](CreateTweetResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_tweet_response import CreateTweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTweetResponse from a JSON string
create_tweet_response_instance = CreateTweetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTweetResponse.to_json())

# convert the object into a dict
create_tweet_response_dict = create_tweet_response_instance.to_dict()
# create an instance of CreateTweetResponse from a dict
create_tweet_response_from_dict = CreateTweetResponse.from_dict(create_tweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



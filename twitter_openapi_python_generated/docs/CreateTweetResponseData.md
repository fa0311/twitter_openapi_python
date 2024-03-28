# CreateTweetResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_tweet** | [**CreateTweetResponseResult**](CreateTweetResponseResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_tweet_response_data import CreateTweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTweetResponseData from a JSON string
create_tweet_response_data_instance = CreateTweetResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateTweetResponseData.to_json())

# convert the object into a dict
create_tweet_response_data_dict = create_tweet_response_data_instance.to_dict()
# create an instance of CreateTweetResponseData from a dict
create_tweet_response_data_form_dict = create_tweet_response_data.from_dict(create_tweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetTweetResultByRestId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorsData**](ErrorsData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_tweet_result_by_rest_id200_response import GetTweetResultByRestId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTweetResultByRestId200Response from a JSON string
get_tweet_result_by_rest_id200_response_instance = GetTweetResultByRestId200Response.from_json(json)
# print the JSON string representation of the object
print(GetTweetResultByRestId200Response.to_json())

# convert the object into a dict
get_tweet_result_by_rest_id200_response_dict = get_tweet_result_by_rest_id200_response_instance.to_dict()
# create an instance of GetTweetResultByRestId200Response from a dict
get_tweet_result_by_rest_id200_response_from_dict = GetTweetResultByRestId200Response.from_dict(get_tweet_result_by_rest_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



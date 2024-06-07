# DeleteRetweetResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retweet_results** | [**DeleteRetweet**](DeleteRetweet.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_retweet_response_result import DeleteRetweetResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRetweetResponseResult from a JSON string
delete_retweet_response_result_instance = DeleteRetweetResponseResult.from_json(json)
# print the JSON string representation of the object
print(DeleteRetweetResponseResult.to_json())

# convert the object into a dict
delete_retweet_response_result_dict = delete_retweet_response_result_instance.to_dict()
# create an instance of DeleteRetweetResponseResult from a dict
delete_retweet_response_result_from_dict = DeleteRetweetResponseResult.from_dict(delete_retweet_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



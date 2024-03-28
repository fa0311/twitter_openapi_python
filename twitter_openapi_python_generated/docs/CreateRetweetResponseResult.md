# CreateRetweetResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retweet_results** | [**CreateRetweet**](CreateRetweet.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_retweet_response_result import CreateRetweetResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetweetResponseResult from a JSON string
create_retweet_response_result_instance = CreateRetweetResponseResult.from_json(json)
# print the JSON string representation of the object
print(CreateRetweetResponseResult.to_json())

# convert the object into a dict
create_retweet_response_result_dict = create_retweet_response_result_instance.to_dict()
# create an instance of CreateRetweetResponseResult from a dict
create_retweet_response_result_form_dict = create_retweet_response_result.from_dict(create_retweet_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateRetweetResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_retweet** | [**CreateRetweetResponseResult**](CreateRetweetResponseResult.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.create_retweet_response_data import CreateRetweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetweetResponseData from a JSON string
create_retweet_response_data_instance = CreateRetweetResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateRetweetResponseData.to_json())

# convert the object into a dict
create_retweet_response_data_dict = create_retweet_response_data_instance.to_dict()
# create an instance of CreateRetweetResponseData from a dict
create_retweet_response_data_from_dict = CreateRetweetResponseData.from_dict(create_retweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeleteRetweetResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_retweet** | [**CreateRetweetResponseResult**](CreateRetweetResponseResult.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.delete_retweet_response_data import DeleteRetweetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRetweetResponseData from a JSON string
delete_retweet_response_data_instance = DeleteRetweetResponseData.from_json(json)
# print the JSON string representation of the object
print DeleteRetweetResponseData.to_json()

# convert the object into a dict
delete_retweet_response_data_dict = delete_retweet_response_data_instance.to_dict()
# create an instance of DeleteRetweetResponseData from a dict
delete_retweet_response_data_form_dict = delete_retweet_response_data.from_dict(delete_retweet_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



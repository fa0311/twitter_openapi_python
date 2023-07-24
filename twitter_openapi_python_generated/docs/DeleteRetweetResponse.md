# DeleteRetweetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteRetweetResponseData**](DeleteRetweetResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.delete_retweet_response import DeleteRetweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRetweetResponse from a JSON string
delete_retweet_response_instance = DeleteRetweetResponse.from_json(json)
# print the JSON string representation of the object
print DeleteRetweetResponse.to_json()

# convert the object into a dict
delete_retweet_response_dict = delete_retweet_response_instance.to_dict()
# create an instance of DeleteRetweetResponse from a dict
delete_retweet_response_form_dict = delete_retweet_response.from_dict(delete_retweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



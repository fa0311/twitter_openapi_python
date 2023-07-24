# CreateRetweetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateRetweetResponseData**](CreateRetweetResponseData.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.create_retweet_response import CreateRetweetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetweetResponse from a JSON string
create_retweet_response_instance = CreateRetweetResponse.from_json(json)
# print the JSON string representation of the object
print CreateRetweetResponse.to_json()

# convert the object into a dict
create_retweet_response_dict = create_retweet_response_instance.to_dict()
# create an instance of CreateRetweetResponse from a dict
create_retweet_response_form_dict = create_retweet_response.from_dict(create_retweet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



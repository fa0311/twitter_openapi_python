# GetRetweeters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetRetweetersResponseData**](TweetRetweetersResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_retweeters200_response import GetRetweeters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRetweeters200Response from a JSON string
get_retweeters200_response_instance = GetRetweeters200Response.from_json(json)
# print the JSON string representation of the object
print GetRetweeters200Response.to_json()

# convert the object into a dict
get_retweeters200_response_dict = get_retweeters200_response_instance.to_dict()
# create an instance of GetRetweeters200Response from a dict
get_retweeters200_response_form_dict = get_retweeters200_response.from_dict(get_retweeters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



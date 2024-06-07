# PostDeleteRetweet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteRetweetResponseData**](DeleteRetweetResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_delete_retweet200_response import PostDeleteRetweet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeleteRetweet200Response from a JSON string
post_delete_retweet200_response_instance = PostDeleteRetweet200Response.from_json(json)
# print the JSON string representation of the object
print(PostDeleteRetweet200Response.to_json())

# convert the object into a dict
post_delete_retweet200_response_dict = post_delete_retweet200_response_instance.to_dict()
# create an instance of PostDeleteRetweet200Response from a dict
post_delete_retweet200_response_from_dict = PostDeleteRetweet200Response.from_dict(post_delete_retweet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



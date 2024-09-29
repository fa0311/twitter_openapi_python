# PostCreateRetweet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorsData**](ErrorsData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_create_retweet200_response import PostCreateRetweet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateRetweet200Response from a JSON string
post_create_retweet200_response_instance = PostCreateRetweet200Response.from_json(json)
# print the JSON string representation of the object
print(PostCreateRetweet200Response.to_json())

# convert the object into a dict
post_create_retweet200_response_dict = post_create_retweet200_response_instance.to_dict()
# create an instance of PostCreateRetweet200Response from a dict
post_create_retweet200_response_from_dict = PostCreateRetweet200Response.from_dict(post_create_retweet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



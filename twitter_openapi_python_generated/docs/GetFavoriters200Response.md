# GetFavoriters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TweetFavoritersResponseData**](TweetFavoritersResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_favoriters200_response import GetFavoriters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFavoriters200Response from a JSON string
get_favoriters200_response_instance = GetFavoriters200Response.from_json(json)
# print the JSON string representation of the object
print GetFavoriters200Response.to_json()

# convert the object into a dict
get_favoriters200_response_dict = get_favoriters200_response_instance.to_dict()
# create an instance of GetFavoriters200Response from a dict
get_favoriters200_response_form_dict = get_favoriters200_response.from_dict(get_favoriters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



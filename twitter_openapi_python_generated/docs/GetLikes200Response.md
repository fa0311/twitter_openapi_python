# GetLikes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorsData**](ErrorsData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_likes200_response import GetLikes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLikes200Response from a JSON string
get_likes200_response_instance = GetLikes200Response.from_json(json)
# print the JSON string representation of the object
print(GetLikes200Response.to_json())

# convert the object into a dict
get_likes200_response_dict = get_likes200_response_instance.to_dict()
# create an instance of GetLikes200Response from a dict
get_likes200_response_from_dict = GetLikes200Response.from_dict(get_likes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



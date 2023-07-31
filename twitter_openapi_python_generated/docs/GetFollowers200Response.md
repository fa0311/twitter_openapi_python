# GetFollowers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FollowResponseData**](FollowResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_followers200_response import GetFollowers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFollowers200Response from a JSON string
get_followers200_response_instance = GetFollowers200Response.from_json(json)
# print the JSON string representation of the object
print GetFollowers200Response.to_json()

# convert the object into a dict
get_followers200_response_dict = get_followers200_response_instance.to_dict()
# create an instance of GetFollowers200Response from a dict
get_followers200_response_form_dict = get_followers200_response.from_dict(get_followers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



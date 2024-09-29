# GetProfileSpotlightsQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ErrorsData**](ErrorsData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.get_profile_spotlights_query200_response import GetProfileSpotlightsQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfileSpotlightsQuery200Response from a JSON string
get_profile_spotlights_query200_response_instance = GetProfileSpotlightsQuery200Response.from_json(json)
# print the JSON string representation of the object
print(GetProfileSpotlightsQuery200Response.to_json())

# convert the object into a dict
get_profile_spotlights_query200_response_dict = get_profile_spotlights_query200_response_instance.to_dict()
# create an instance of GetProfileSpotlightsQuery200Response from a dict
get_profile_spotlights_query200_response_from_dict = GetProfileSpotlightsQuery200Response.from_dict(get_profile_spotlights_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



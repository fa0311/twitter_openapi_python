# SocialContextLandingUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**url_type** | **str** |  | [optional] 
**urt_endpoint_options** | [**UrtEndpointOptions**](UrtEndpointOptions.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.social_context_landing_url import SocialContextLandingUrl

# TODO update the JSON string below
json = "{}"
# create an instance of SocialContextLandingUrl from a JSON string
social_context_landing_url_instance = SocialContextLandingUrl.from_json(json)
# print the JSON string representation of the object
print(SocialContextLandingUrl.to_json())

# convert the object into a dict
social_context_landing_url_dict = social_context_landing_url_instance.to_dict()
# create an instance of SocialContextLandingUrl from a dict
social_context_landing_url_from_dict = SocialContextLandingUrl.from_dict(social_context_landing_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



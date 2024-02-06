# SocialContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.social_context import SocialContext

# TODO update the JSON string below
json = "{}"
# create an instance of SocialContext from a JSON string
social_context_instance = SocialContext.from_json(json)
# print the JSON string representation of the object
print SocialContext.to_json()

# convert the object into a dict
social_context_dict = social_context_instance.to_dict()
# create an instance of SocialContext from a dict
social_context_form_dict = social_context.from_dict(social_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



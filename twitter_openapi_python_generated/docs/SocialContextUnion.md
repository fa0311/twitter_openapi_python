# SocialContextUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** |  | [optional] 
**landing_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | [optional] 
**text** | **str** |  | [optional] 
**type** | [**SocialContextUnionType**](SocialContextUnionType.md) |  | [optional] 
**functionality_type** | **str** |  | [optional] 
**topic** | [**TopicContext**](TopicContext.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.social_context_union import SocialContextUnion

# TODO update the JSON string below
json = "{}"
# create an instance of SocialContextUnion from a JSON string
social_context_union_instance = SocialContextUnion.from_json(json)
# print the JSON string representation of the object
print(SocialContextUnion.to_json())

# convert the object into a dict
social_context_union_dict = social_context_union_instance.to_dict()
# create an instance of SocialContextUnion from a dict
social_context_union_form_dict = social_context_union.from_dict(social_context_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



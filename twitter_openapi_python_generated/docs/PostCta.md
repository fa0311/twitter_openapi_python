# PostCta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_url** | **str** |  | 
**background_color** | **str** |  | 
**show_chevron** | **bool** |  | 
**stroke_color** | **str** |  | 
**title_text** | [**PostCtaTitleText**](PostCtaTitleText.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_cta import PostCta

# TODO update the JSON string below
json = "{}"
# create an instance of PostCta from a JSON string
post_cta_instance = PostCta.from_json(json)
# print the JSON string representation of the object
print(PostCta.to_json())

# convert the object into a dict
post_cta_dict = post_cta_instance.to_dict()
# create an instance of PostCta from a dict
post_cta_from_dict = PostCta.from_dict(post_cta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



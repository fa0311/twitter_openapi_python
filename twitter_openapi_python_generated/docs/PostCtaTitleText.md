# PostCtaTitleText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[PostCtaTitleTextEntity]**](PostCtaTitleTextEntity.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_cta_title_text import PostCtaTitleText

# TODO update the JSON string below
json = "{}"
# create an instance of PostCtaTitleText from a JSON string
post_cta_title_text_instance = PostCtaTitleText.from_json(json)
# print the JSON string representation of the object
print(PostCtaTitleText.to_json())

# convert the object into a dict
post_cta_title_text_dict = post_cta_title_text_instance.to_dict()
# create an instance of PostCtaTitleText from a dict
post_cta_title_text_from_dict = PostCtaTitleText.from_dict(post_cta_title_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



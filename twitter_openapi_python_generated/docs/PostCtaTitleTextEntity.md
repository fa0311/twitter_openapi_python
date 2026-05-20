# PostCtaTitleTextEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**PostCtaTitleTextEntityRef**](PostCtaTitleTextEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.post_cta_title_text_entity import PostCtaTitleTextEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PostCtaTitleTextEntity from a JSON string
post_cta_title_text_entity_instance = PostCtaTitleTextEntity.from_json(json)
# print the JSON string representation of the object
print(PostCtaTitleTextEntity.to_json())

# convert the object into a dict
post_cta_title_text_entity_dict = post_cta_title_text_entity_instance.to_dict()
# create an instance of PostCtaTitleTextEntity from a dict
post_cta_title_text_entity_from_dict = PostCtaTitleTextEntity.from_dict(post_cta_title_text_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



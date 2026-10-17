# ArticleContentState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[ArticleContentBlock]**](ArticleContentBlock.md) |  | 
**entity_map** | [**List[ArticleContentEntity]**](ArticleContentEntity.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_state import ArticleContentState

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentState from a JSON string
article_content_state_instance = ArticleContentState.from_json(json)
# print the JSON string representation of the object
print(ArticleContentState.to_json())

# convert the object into a dict
article_content_state_dict = article_content_state_instance.to_dict()
# create an instance of ArticleContentState from a dict
article_content_state_from_dict = ArticleContentState.from_dict(article_content_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



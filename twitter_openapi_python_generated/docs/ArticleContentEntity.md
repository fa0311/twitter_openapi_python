# ArticleContentEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | [**ArticleContentEntityValue**](ArticleContentEntityValue.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_entity import ArticleContentEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentEntity from a JSON string
article_content_entity_instance = ArticleContentEntity.from_json(json)
# print the JSON string representation of the object
print(ArticleContentEntity.to_json())

# convert the object into a dict
article_content_entity_dict = article_content_entity_instance.to_dict()
# create an instance of ArticleContentEntity from a dict
article_content_entity_from_dict = ArticleContentEntity.from_dict(article_content_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



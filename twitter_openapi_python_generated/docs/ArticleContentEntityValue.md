# ArticleContentEntityValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArticleContentEntityData**](ArticleContentEntityData.md) |  | 
**mutability** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_entity_value import ArticleContentEntityValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentEntityValue from a JSON string
article_content_entity_value_instance = ArticleContentEntityValue.from_json(json)
# print the JSON string representation of the object
print(ArticleContentEntityValue.to_json())

# convert the object into a dict
article_content_entity_value_dict = article_content_entity_value_instance.to_dict()
# create an instance of ArticleContentEntityValue from a dict
article_content_entity_value_from_dict = ArticleContentEntityValue.from_dict(article_content_entity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArticleContentEntityRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** |  | 
**length** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_entity_range import ArticleContentEntityRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentEntityRange from a JSON string
article_content_entity_range_instance = ArticleContentEntityRange.from_json(json)
# print the JSON string representation of the object
print(ArticleContentEntityRange.to_json())

# convert the object into a dict
article_content_entity_range_dict = article_content_entity_range_instance.to_dict()
# create an instance of ArticleContentEntityRange from a dict
article_content_entity_range_from_dict = ArticleContentEntityRange.from_dict(article_content_entity_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



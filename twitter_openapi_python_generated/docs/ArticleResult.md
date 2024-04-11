# ArticleResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_media** | [**ArticleCoverMedia**](ArticleCoverMedia.md) |  | 
**id** | **str** |  | 
**preview_text** | **str** |  | 
**rest_id** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_result import ArticleResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleResult from a JSON string
article_result_instance = ArticleResult.from_json(json)
# print the JSON string representation of the object
print(ArticleResult.to_json())

# convert the object into a dict
article_result_dict = article_result_instance.to_dict()
# create an instance of ArticleResult from a dict
article_result_form_dict = article_result.from_dict(article_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



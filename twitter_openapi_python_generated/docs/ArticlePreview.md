# ArticlePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **int** |  | 
**cover_media** | [**ArticleCoverMedia**](ArticleCoverMedia.md) |  | [optional] 
**preview_text** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_preview import ArticlePreview

# TODO update the JSON string below
json = "{}"
# create an instance of ArticlePreview from a JSON string
article_preview_instance = ArticlePreview.from_json(json)
# print the JSON string representation of the object
print(ArticlePreview.to_json())

# convert the object into a dict
article_preview_dict = article_preview_instance.to_dict()
# create an instance of ArticlePreview from a dict
article_preview_from_dict = ArticlePreview.from_dict(article_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



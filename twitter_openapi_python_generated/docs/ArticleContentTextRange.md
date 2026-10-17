# ArticleContentTextRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**text** | **str** |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_text_range import ArticleContentTextRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentTextRange from a JSON string
article_content_text_range_instance = ArticleContentTextRange.from_json(json)
# print the JSON string representation of the object
print(ArticleContentTextRange.to_json())

# convert the object into a dict
article_content_text_range_dict = article_content_text_range_instance.to_dict()
# create an instance of ArticleContentTextRange from a dict
article_content_text_range_from_dict = ArticleContentTextRange.from_dict(article_content_text_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



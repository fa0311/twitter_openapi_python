# ArticleContentBlockData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentions** | [**List[ArticleContentTextRange]**](ArticleContentTextRange.md) |  | [optional] 
**urls** | [**List[ArticleContentTextRange]**](ArticleContentTextRange.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.article_content_block_data import ArticleContentBlockData

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentBlockData from a JSON string
article_content_block_data_instance = ArticleContentBlockData.from_json(json)
# print the JSON string representation of the object
print(ArticleContentBlockData.to_json())

# convert the object into a dict
article_content_block_data_dict = article_content_block_data_instance.to_dict()
# create an instance of ArticleContentBlockData from a dict
article_content_block_data_from_dict = ArticleContentBlockData.from_dict(article_content_block_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



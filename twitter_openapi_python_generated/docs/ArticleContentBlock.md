# ArticleContentBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArticleContentBlockData**](ArticleContentBlockData.md) |  | 
**entity_ranges** | [**List[ArticleContentEntityRange]**](ArticleContentEntityRange.md) |  | 
**inline_style_ranges** | [**List[ArticleContentInlineStyleRange]**](ArticleContentInlineStyleRange.md) |  | 
**key** | **str** |  | 
**text** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_block import ArticleContentBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentBlock from a JSON string
article_content_block_instance = ArticleContentBlock.from_json(json)
# print the JSON string representation of the object
print(ArticleContentBlock.to_json())

# convert the object into a dict
article_content_block_dict = article_content_block_instance.to_dict()
# create an instance of ArticleContentBlock from a dict
article_content_block_from_dict = ArticleContentBlock.from_dict(article_content_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



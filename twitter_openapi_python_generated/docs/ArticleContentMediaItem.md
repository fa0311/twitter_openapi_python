# ArticleContentMediaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_media_id** | **str** |  | 
**media_category** | **str** |  | 
**media_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_content_media_item import ArticleContentMediaItem

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentMediaItem from a JSON string
article_content_media_item_instance = ArticleContentMediaItem.from_json(json)
# print the JSON string representation of the object
print(ArticleContentMediaItem.to_json())

# convert the object into a dict
article_content_media_item_dict = article_content_media_item_instance.to_dict()
# create an instance of ArticleContentMediaItem from a dict
article_content_media_item_from_dict = ArticleContentMediaItem.from_dict(article_content_media_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



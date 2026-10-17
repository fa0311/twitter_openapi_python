# ArticleContentEntityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**entity_key** | **str** |  | [optional] 
**media_items** | [**List[ArticleContentMediaItem]**](ArticleContentMediaItem.md) |  | [optional] 
**tweet_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.article_content_entity_data import ArticleContentEntityData

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleContentEntityData from a JSON string
article_content_entity_data_instance = ArticleContentEntityData.from_json(json)
# print the JSON string representation of the object
print(ArticleContentEntityData.to_json())

# convert the object into a dict
article_content_entity_data_dict = article_content_entity_data_instance.to_dict()
# create an instance of ArticleContentEntityData from a dict
article_content_entity_data_from_dict = ArticleContentEntityData.from_dict(article_content_entity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



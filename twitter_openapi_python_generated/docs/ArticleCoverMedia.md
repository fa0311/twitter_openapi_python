# ArticleCoverMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**media_id** | **str** |  | 
**media_info** | [**ArticleCoverMediaInfo**](ArticleCoverMediaInfo.md) |  | 
**media_key** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_cover_media import ArticleCoverMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleCoverMedia from a JSON string
article_cover_media_instance = ArticleCoverMedia.from_json(json)
# print the JSON string representation of the object
print(ArticleCoverMedia.to_json())

# convert the object into a dict
article_cover_media_dict = article_cover_media_instance.to_dict()
# create an instance of ArticleCoverMedia from a dict
article_cover_media_form_dict = article_cover_media.from_dict(article_cover_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



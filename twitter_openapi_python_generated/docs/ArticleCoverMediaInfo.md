# ArticleCoverMediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | [optional] 
**color_info** | [**ArticleCoverMediaColorInfo**](ArticleCoverMediaColorInfo.md) |  | 
**original_img_height** | **int** |  | 
**original_img_url** | **str** |  | 
**original_img_width** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.article_cover_media_info import ArticleCoverMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleCoverMediaInfo from a JSON string
article_cover_media_info_instance = ArticleCoverMediaInfo.from_json(json)
# print the JSON string representation of the object
print(ArticleCoverMediaInfo.to_json())

# convert the object into a dict
article_cover_media_info_dict = article_cover_media_info_instance.to_dict()
# create an instance of ArticleCoverMediaInfo from a dict
article_cover_media_info_form_dict = article_cover_media_info.from_dict(article_cover_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



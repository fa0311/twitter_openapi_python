# ThumbnailImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_img_height** | **int** |  | [optional] 
**original_img_url** | **str** |  | [optional] 
**original_img_width** | **int** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.thumbnail_image import ThumbnailImage

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailImage from a JSON string
thumbnail_image_instance = ThumbnailImage.from_json(json)
# print the JSON string representation of the object
print(ThumbnailImage.to_json())

# convert the object into a dict
thumbnail_image_dict = thumbnail_image_instance.to_dict()
# create an instance of ThumbnailImage from a dict
thumbnail_image_from_dict = ThumbnailImage.from_dict(thumbnail_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



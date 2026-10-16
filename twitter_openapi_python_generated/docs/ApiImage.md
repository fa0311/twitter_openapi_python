# ApiImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**color_info** | [**MediaColorInfo**](MediaColorInfo.md) |  | 
**original_img_height** | **int** |  | 
**original_img_url** | **str** |  | 
**original_img_width** | **int** |  | 
**salient_rect** | [**MediaSalientRect**](MediaSalientRect.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.api_image import ApiImage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiImage from a JSON string
api_image_instance = ApiImage.from_json(json)
# print the JSON string representation of the object
print(ApiImage.to_json())

# convert the object into a dict
api_image_dict = api_image_instance.to_dict()
# create an instance of ApiImage from a dict
api_image_from_dict = ApiImage.from_dict(api_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



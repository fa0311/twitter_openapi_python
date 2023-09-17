# MediaOriginalInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**focus_rects** | [**List[MediaOriginalInfoFocusRect]**](MediaOriginalInfoFocusRect.md) |  | [optional] 
**height** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.media_original_info import MediaOriginalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaOriginalInfo from a JSON string
media_original_info_instance = MediaOriginalInfo.from_json(json)
# print the JSON string representation of the object
print MediaOriginalInfo.to_json()

# convert the object into a dict
media_original_info_dict = media_original_info_instance.to_dict()
# create an instance of MediaOriginalInfo from a dict
media_original_info_form_dict = media_original_info.from_dict(media_original_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



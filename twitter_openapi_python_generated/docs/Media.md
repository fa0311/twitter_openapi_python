# Media


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_media_info** | **Dict[str, object]** |  | [optional] 
**display_url** | **str** |  | 
**expanded_url** | **str** |  | 
**ext_alt_text** | **str** |  | [optional] 
**ext_media_availability** | [**ExtMediaAvailability**](ExtMediaAvailability.md) |  | 
**features** | **object** |  | [optional] 
**id_str** | **str** |  | 
**indices** | **List[int]** |  | 
**media_key** | **str** |  | 
**media_url_https** | **str** |  | 
**original_info** | [**MediaOriginalInfo**](MediaOriginalInfo.md) |  | 
**sensitive_media_warning** | [**SensitiveMediaWarning**](SensitiveMediaWarning.md) |  | [optional] 
**sizes** | [**MediaSizes**](MediaSizes.md) |  | 
**source_status_id_str** | **str** |  | [optional] 
**source_user_id_str** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | 
**video_info** | **Dict[str, object]** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.media import Media

# TODO update the JSON string below
json = "{}"
# create an instance of Media from a JSON string
media_instance = Media.from_json(json)
# print the JSON string representation of the object
print Media.to_json()

# convert the object into a dict
media_dict = media_instance.to_dict()
# create an instance of Media from a dict
media_form_dict = media.from_dict(media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



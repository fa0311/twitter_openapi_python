# MediaExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_media_info** | [**AdditionalMediaInfo**](AdditionalMediaInfo.md) |  | [optional] 
**allow_download_status** | [**AllowDownloadStatus**](AllowDownloadStatus.md) |  | [optional] 
**display_url** | **str** |  | 
**expanded_url** | **str** |  | 
**ext_alt_text** | **str** |  | [optional] 
**ext_media_availability** | [**ExtMediaAvailability**](ExtMediaAvailability.md) |  | [optional] 
**features** | **object** |  | [optional] 
**id_str** | **str** |  | 
**indices** | **List[int]** |  | 
**media_stats** | [**MediaStats**](MediaStats.md) |  | [optional] 
**media_key** | **str** |  | 
**media_results** | [**MediaResults**](MediaResults.md) |  | [optional] 
**media_url_https** | **str** |  | 
**original_info** | [**MediaOriginalInfo**](MediaOriginalInfo.md) |  | 
**sensitive_media_warning** | [**SensitiveMediaWarning**](SensitiveMediaWarning.md) |  | [optional] 
**sizes** | [**MediaSizes**](MediaSizes.md) |  | 
**source_status_id_str** | **str** |  | [optional] 
**source_user_id_str** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | 
**video_info** | [**MediaVideoInfo**](MediaVideoInfo.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.media_extended import MediaExtended

# TODO update the JSON string below
json = "{}"
# create an instance of MediaExtended from a JSON string
media_extended_instance = MediaExtended.from_json(json)
# print the JSON string representation of the object
print(MediaExtended.to_json())

# convert the object into a dict
media_extended_dict = media_extended_instance.to_dict()
# create an instance of MediaExtended from a dict
media_extended_from_dict = MediaExtended.from_dict(media_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



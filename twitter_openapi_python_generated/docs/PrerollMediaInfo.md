# PrerollMediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_name** | **str** |  | 
**advertiser_profile_image_url** | **str** |  | 
**call_to_action** | [**PrerollCallToAction**](PrerollCallToAction.md) |  | 
**duration_millis** | **int** |  | 
**publisher_results** | [**UserResults**](UserResults.md) |  | 
**render_ad_by_advertiser_name** | **bool** |  | 
**uuid** | **str** |  | 
**video_variants** | [**List[PrerollVideoVariant]**](PrerollVideoVariant.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.preroll_media_info import PrerollMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PrerollMediaInfo from a JSON string
preroll_media_info_instance = PrerollMediaInfo.from_json(json)
# print the JSON string representation of the object
print(PrerollMediaInfo.to_json())

# convert the object into a dict
preroll_media_info_dict = preroll_media_info_instance.to_dict()
# create an instance of PrerollMediaInfo from a dict
preroll_media_info_from_dict = PrerollMediaInfo.from_dict(preroll_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



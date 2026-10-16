# AdMetadataContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_url_params** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 
**is_quick_promote** | **bool** |  | 
**render_legacy_website_card** | **bool** |  | 
**render_sales_cta_website_card** | **bool** |  | 
**show_overlay_on_first_card** | **bool** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.ad_metadata_container import AdMetadataContainer

# TODO update the JSON string below
json = "{}"
# create an instance of AdMetadataContainer from a JSON string
ad_metadata_container_instance = AdMetadataContainer.from_json(json)
# print the JSON string representation of the object
print(AdMetadataContainer.to_json())

# convert the object into a dict
ad_metadata_container_dict = ad_metadata_container_instance.to_dict()
# create an instance of AdMetadataContainer from a dict
ad_metadata_container_from_dict = AdMetadataContainer.from_dict(ad_metadata_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PromotedMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_metadata_container** | [**AdMetadataContainer**](AdMetadataContainer.md) |  | 
**advertiser_results** | [**UserResults**](UserResults.md) |  | 
**click_tracking_info** | [**ClickTrackingInfo**](ClickTrackingInfo.md) |  | 
**impression_id** | **str** |  | 
**impression_string** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.promoted_metadata import PromotedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PromotedMetadata from a JSON string
promoted_metadata_instance = PromotedMetadata.from_json(json)
# print the JSON string representation of the object
print(PromotedMetadata.to_json())

# convert the object into a dict
promoted_metadata_dict = promoted_metadata_instance.to_dict()
# create an instance of PromotedMetadata from a dict
promoted_metadata_from_dict = PromotedMetadata.from_dict(promoted_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



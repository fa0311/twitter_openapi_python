# TrendPromotedMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_results** | [**UserResults**](UserResults.md) |  | 
**disclosure_type** | **str** |  | 
**impression_id** | **str** |  | 
**impression_string** | **str** |  | 
**promoted_trend** | [**PromotedTrend**](PromotedTrend.md) |  | 
**promoted_trend_description** | **str** |  | 
**promoted_trend_name** | **str** |  | 
**promoted_trend_query_term** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.trend_promoted_metadata import TrendPromotedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrendPromotedMetadata from a JSON string
trend_promoted_metadata_instance = TrendPromotedMetadata.from_json(json)
# print the JSON string representation of the object
print(TrendPromotedMetadata.to_json())

# convert the object into a dict
trend_promoted_metadata_dict = trend_promoted_metadata_instance.to_dict()
# create an instance of TrendPromotedMetadata from a dict
trend_promoted_metadata_from_dict = TrendPromotedMetadata.from_dict(trend_promoted_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



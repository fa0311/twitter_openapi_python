# TimelineTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**images** | [**List[TrendImage]**](TrendImage.md) |  | [optional] 
**is_ai_trend** | **bool** |  | [optional] 
**item_type** | [**ContentItemType**](ContentItemType.md) |  | [optional] 
**name** | **str** |  | 
**social_context** | [**SocialContextUnion**](SocialContextUnion.md) |  | [optional] 
**thumbnail_image** | [**ThumbnailImage**](ThumbnailImage.md) |  | [optional] 
**trend_metadata** | [**TrendMetadata**](TrendMetadata.md) |  | 
**trend_url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.timeline_trend import TimelineTrend

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineTrend from a JSON string
timeline_trend_instance = TimelineTrend.from_json(json)
# print the JSON string representation of the object
print(TimelineTrend.to_json())

# convert the object into a dict
timeline_trend_dict = timeline_trend_instance.to_dict()
# create an instance of TimelineTrend from a dict
timeline_trend_from_dict = TimelineTrend.from_dict(timeline_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AiTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**core** | [**AiTrendCore**](AiTrendCore.md) |  | 
**id** | **str** |  | 
**post_count** | **str** |  | 
**rest_id** | **str** |  | 
**social_proof** | [**List[AiTrendSocialProof]**](AiTrendSocialProof.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.ai_trend import AiTrend

# TODO update the JSON string below
json = "{}"
# create an instance of AiTrend from a JSON string
ai_trend_instance = AiTrend.from_json(json)
# print the JSON string representation of the object
print(AiTrend.to_json())

# convert the object into a dict
ai_trend_dict = ai_trend_instance.to_dict()
# create an instance of AiTrend from a dict
ai_trend_from_dict = AiTrend.from_dict(ai_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



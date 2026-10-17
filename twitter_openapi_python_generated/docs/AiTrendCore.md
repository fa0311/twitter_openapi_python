# AiTrendCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | 
**created_at_ms** | **int** |  | 
**hook** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.ai_trend_core import AiTrendCore

# TODO update the JSON string below
json = "{}"
# create an instance of AiTrendCore from a JSON string
ai_trend_core_instance = AiTrendCore.from_json(json)
# print the JSON string representation of the object
print(AiTrendCore.to_json())

# convert the object into a dict
ai_trend_core_dict = ai_trend_core_instance.to_dict()
# create an instance of AiTrendCore from a dict
ai_trend_core_from_dict = AiTrendCore.from_dict(ai_trend_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



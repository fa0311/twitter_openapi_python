# AiTrendResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**result** | [**AiTrend**](AiTrend.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.ai_trend_results import AiTrendResults

# TODO update the JSON string below
json = "{}"
# create an instance of AiTrendResults from a JSON string
ai_trend_results_instance = AiTrendResults.from_json(json)
# print the JSON string representation of the object
print(AiTrendResults.to_json())

# convert the object into a dict
ai_trend_results_dict = ai_trend_results_instance.to_dict()
# create an instance of AiTrendResults from a dict
ai_trend_results_from_dict = AiTrendResults.from_dict(ai_trend_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



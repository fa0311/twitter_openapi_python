# GroupedTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.grouped_trend import GroupedTrend

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedTrend from a JSON string
grouped_trend_instance = GroupedTrend.from_json(json)
# print the JSON string representation of the object
print(GroupedTrend.to_json())

# convert the object into a dict
grouped_trend_dict = grouped_trend_instance.to_dict()
# create an instance of GroupedTrend from a dict
grouped_trend_from_dict = GroupedTrend.from_dict(grouped_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



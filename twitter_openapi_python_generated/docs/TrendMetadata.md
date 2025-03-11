# TrendMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | [**SocialContextLandingUrl**](SocialContextLandingUrl.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.trend_metadata import TrendMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrendMetadata from a JSON string
trend_metadata_instance = TrendMetadata.from_json(json)
# print the JSON string representation of the object
print(TrendMetadata.to_json())

# convert the object into a dict
trend_metadata_dict = trend_metadata_instance.to_dict()
# create an instance of TrendMetadata from a dict
trend_metadata_from_dict = TrendMetadata.from_dict(trend_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



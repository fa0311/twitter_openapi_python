# ClickTrackingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_params** | [**List[KeyValue]**](KeyValue.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.click_tracking_info import ClickTrackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClickTrackingInfo from a JSON string
click_tracking_info_instance = ClickTrackingInfo.from_json(json)
# print the JSON string representation of the object
print(ClickTrackingInfo.to_json())

# convert the object into a dict
click_tracking_info_dict = click_tracking_info_instance.to_dict()
# create an instance of ClickTrackingInfo from a dict
click_tracking_info_from_dict = ClickTrackingInfo.from_dict(click_tracking_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HomeTimelineResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**HomeTimelineHome**](HomeTimelineHome.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.home_timeline_response_data import HomeTimelineResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of HomeTimelineResponseData from a JSON string
home_timeline_response_data_instance = HomeTimelineResponseData.from_json(json)
# print the JSON string representation of the object
print(HomeTimelineResponseData.to_json())

# convert the object into a dict
home_timeline_response_data_dict = home_timeline_response_data_instance.to_dict()
# create an instance of HomeTimelineResponseData from a dict
home_timeline_response_data_from_dict = HomeTimelineResponseData.from_dict(home_timeline_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



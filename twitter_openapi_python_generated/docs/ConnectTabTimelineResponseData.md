# ConnectTabTimelineResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_tab_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.connect_tab_timeline_response_data import ConnectTabTimelineResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTabTimelineResponseData from a JSON string
connect_tab_timeline_response_data_instance = ConnectTabTimelineResponseData.from_json(json)
# print the JSON string representation of the object
print(ConnectTabTimelineResponseData.to_json())

# convert the object into a dict
connect_tab_timeline_response_data_dict = connect_tab_timeline_response_data_instance.to_dict()
# create an instance of ConnectTabTimelineResponseData from a dict
connect_tab_timeline_response_data_from_dict = ConnectTabTimelineResponseData.from_dict(connect_tab_timeline_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



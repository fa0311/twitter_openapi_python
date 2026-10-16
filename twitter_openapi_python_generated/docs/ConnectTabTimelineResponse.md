# ConnectTabTimelineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ConnectTabTimelineResponseData**](ConnectTabTimelineResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.connect_tab_timeline_response import ConnectTabTimelineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTabTimelineResponse from a JSON string
connect_tab_timeline_response_instance = ConnectTabTimelineResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectTabTimelineResponse.to_json())

# convert the object into a dict
connect_tab_timeline_response_dict = connect_tab_timeline_response_instance.to_dict()
# create an instance of ConnectTabTimelineResponse from a dict
connect_tab_timeline_response_from_dict = ConnectTabTimelineResponse.from_dict(connect_tab_timeline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



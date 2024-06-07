# ClientEventInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] 
**details** | **Dict[str, object]** |  | [optional] 
**element** | **str** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.client_event_info import ClientEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEventInfo from a JSON string
client_event_info_instance = ClientEventInfo.from_json(json)
# print the JSON string representation of the object
print(ClientEventInfo.to_json())

# convert the object into a dict
client_event_info_dict = client_event_info_instance.to_dict()
# create an instance of ClientEventInfo from a dict
client_event_info_from_dict = ClientEventInfo.from_dict(client_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



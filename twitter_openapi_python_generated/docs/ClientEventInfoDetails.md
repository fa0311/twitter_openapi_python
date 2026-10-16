# ClientEventInfoDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_details** | [**ConversationDetails**](ConversationDetails.md) |  | [optional] 
**timelines_details** | [**TimelinesDetails**](TimelinesDetails.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.client_event_info_details import ClientEventInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEventInfoDetails from a JSON string
client_event_info_details_instance = ClientEventInfoDetails.from_json(json)
# print the JSON string representation of the object
print(ClientEventInfoDetails.to_json())

# convert the object into a dict
client_event_info_details_dict = client_event_info_details_instance.to_dict()
# create an instance of ClientEventInfoDetails from a dict
client_event_info_details_from_dict = ClientEventInfoDetails.from_dict(client_event_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



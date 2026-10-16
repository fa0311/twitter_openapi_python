# ListSubscribersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ListSubscribersList**](ListSubscribersList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_subscribers_response_data import ListSubscribersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubscribersResponseData from a JSON string
list_subscribers_response_data_instance = ListSubscribersResponseData.from_json(json)
# print the JSON string representation of the object
print(ListSubscribersResponseData.to_json())

# convert the object into a dict
list_subscribers_response_data_dict = list_subscribers_response_data_instance.to_dict()
# create an instance of ListSubscribersResponseData from a dict
list_subscribers_response_data_from_dict = ListSubscribersResponseData.from_dict(list_subscribers_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListSubscribersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ListSubscribersResponseData**](ListSubscribersResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.list_subscribers_response import ListSubscribersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSubscribersResponse from a JSON string
list_subscribers_response_instance = ListSubscribersResponse.from_json(json)
# print the JSON string representation of the object
print(ListSubscribersResponse.to_json())

# convert the object into a dict
list_subscribers_response_dict = list_subscribers_response_instance.to_dict()
# create an instance of ListSubscribersResponse from a dict
list_subscribers_response_from_dict = ListSubscribersResponse.from_dict(list_subscribers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



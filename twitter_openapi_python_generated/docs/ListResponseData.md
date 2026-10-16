# ListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**TwitterList**](TwitterList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_response_data import ListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseData from a JSON string
list_response_data_instance = ListResponseData.from_json(json)
# print the JSON string representation of the object
print(ListResponseData.to_json())

# convert the object into a dict
list_response_data_dict = list_response_data_instance.to_dict()
# create an instance of ListResponseData from a dict
list_response_data_from_dict = ListResponseData.from_dict(list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



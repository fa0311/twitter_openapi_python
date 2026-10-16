# DataSaverModeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DataSaverModeResponseData**](DataSaverModeResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.data_saver_mode_response import DataSaverModeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataSaverModeResponse from a JSON string
data_saver_mode_response_instance = DataSaverModeResponse.from_json(json)
# print the JSON string representation of the object
print(DataSaverModeResponse.to_json())

# convert the object into a dict
data_saver_mode_response_dict = data_saver_mode_response_instance.to_dict()
# create an instance of DataSaverModeResponse from a dict
data_saver_mode_response_from_dict = DataSaverModeResponse.from_dict(data_saver_mode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BirdwatchFetchAliasSelfSelectStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BirdwatchFetchAliasSelfSelectStatusResponseData**](BirdwatchFetchAliasSelfSelectStatusResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_alias_self_select_status_response import BirdwatchFetchAliasSelfSelectStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchAliasSelfSelectStatusResponse from a JSON string
birdwatch_fetch_alias_self_select_status_response_instance = BirdwatchFetchAliasSelfSelectStatusResponse.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchAliasSelfSelectStatusResponse.to_json())

# convert the object into a dict
birdwatch_fetch_alias_self_select_status_response_dict = birdwatch_fetch_alias_self_select_status_response_instance.to_dict()
# create an instance of BirdwatchFetchAliasSelfSelectStatusResponse from a dict
birdwatch_fetch_alias_self_select_status_response_from_dict = BirdwatchFetchAliasSelfSelectStatusResponse.from_dict(birdwatch_fetch_alias_self_select_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



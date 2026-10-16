# BirdwatchFetchPublicDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BirdwatchFetchPublicDataResponseData**](BirdwatchFetchPublicDataResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_public_data_response import BirdwatchFetchPublicDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchPublicDataResponse from a JSON string
birdwatch_fetch_public_data_response_instance = BirdwatchFetchPublicDataResponse.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchPublicDataResponse.to_json())

# convert the object into a dict
birdwatch_fetch_public_data_response_dict = birdwatch_fetch_public_data_response_instance.to_dict()
# create an instance of BirdwatchFetchPublicDataResponse from a dict
birdwatch_fetch_public_data_response_from_dict = BirdwatchFetchPublicDataResponse.from_dict(birdwatch_fetch_public_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



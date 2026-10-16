# BirdwatchFetchBirdwatchProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BirdwatchFetchBirdwatchProfileResponseData**](BirdwatchFetchBirdwatchProfileResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_birdwatch_profile_response import BirdwatchFetchBirdwatchProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchBirdwatchProfileResponse from a JSON string
birdwatch_fetch_birdwatch_profile_response_instance = BirdwatchFetchBirdwatchProfileResponse.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchBirdwatchProfileResponse.to_json())

# convert the object into a dict
birdwatch_fetch_birdwatch_profile_response_dict = birdwatch_fetch_birdwatch_profile_response_instance.to_dict()
# create an instance of BirdwatchFetchBirdwatchProfileResponse from a dict
birdwatch_fetch_birdwatch_profile_response_from_dict = BirdwatchFetchBirdwatchProfileResponse.from_dict(birdwatch_fetch_birdwatch_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



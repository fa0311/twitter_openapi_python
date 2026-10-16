# BirdwatchFetchAuthenticatedUserProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BirdwatchFetchAuthenticatedUserProfileResponseData**](BirdwatchFetchAuthenticatedUserProfileResponseData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_authenticated_user_profile_response import BirdwatchFetchAuthenticatedUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchAuthenticatedUserProfileResponse from a JSON string
birdwatch_fetch_authenticated_user_profile_response_instance = BirdwatchFetchAuthenticatedUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchAuthenticatedUserProfileResponse.to_json())

# convert the object into a dict
birdwatch_fetch_authenticated_user_profile_response_dict = birdwatch_fetch_authenticated_user_profile_response_instance.to_dict()
# create an instance of BirdwatchFetchAuthenticatedUserProfileResponse from a dict
birdwatch_fetch_authenticated_user_profile_response_from_dict = BirdwatchFetchAuthenticatedUserProfileResponse.from_dict(birdwatch_fetch_authenticated_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



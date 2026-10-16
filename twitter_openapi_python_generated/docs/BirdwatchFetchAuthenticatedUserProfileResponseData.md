# BirdwatchFetchAuthenticatedUserProfileResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated_user_birdwatch_profile** | [**BirdwatchProfile**](BirdwatchProfile.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_authenticated_user_profile_response_data import BirdwatchFetchAuthenticatedUserProfileResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchAuthenticatedUserProfileResponseData from a JSON string
birdwatch_fetch_authenticated_user_profile_response_data_instance = BirdwatchFetchAuthenticatedUserProfileResponseData.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchAuthenticatedUserProfileResponseData.to_json())

# convert the object into a dict
birdwatch_fetch_authenticated_user_profile_response_data_dict = birdwatch_fetch_authenticated_user_profile_response_data_instance.to_dict()
# create an instance of BirdwatchFetchAuthenticatedUserProfileResponseData from a dict
birdwatch_fetch_authenticated_user_profile_response_data_from_dict = BirdwatchFetchAuthenticatedUserProfileResponseData.from_dict(birdwatch_fetch_authenticated_user_profile_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



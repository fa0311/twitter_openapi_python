# BirdwatchFetchPublicDataResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birdwatch_latest_public_data_file_bundle** | [**BirdwatchPublicDataFileBundle**](BirdwatchPublicDataFileBundle.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_fetch_public_data_response_data import BirdwatchFetchPublicDataResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchFetchPublicDataResponseData from a JSON string
birdwatch_fetch_public_data_response_data_instance = BirdwatchFetchPublicDataResponseData.from_json(json)
# print the JSON string representation of the object
print(BirdwatchFetchPublicDataResponseData.to_json())

# convert the object into a dict
birdwatch_fetch_public_data_response_data_dict = birdwatch_fetch_public_data_response_data_instance.to_dict()
# create an instance of BirdwatchFetchPublicDataResponseData from a dict
birdwatch_fetch_public_data_response_data_from_dict = BirdwatchFetchPublicDataResponseData.from_dict(birdwatch_fetch_public_data_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



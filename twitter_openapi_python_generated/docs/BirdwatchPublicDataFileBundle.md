# BirdwatchPublicDataFileBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bat_signals** | [**BirdwatchPublicDataFile**](BirdwatchPublicDataFile.md) |  | 
**note_status_history** | [**BirdwatchPublicDataFile**](BirdwatchPublicDataFile.md) |  | 
**notes** | [**BirdwatchPublicDataFile**](BirdwatchPublicDataFile.md) |  | 
**ratings** | [**BirdwatchPublicDataFile**](BirdwatchPublicDataFile.md) |  | 
**user_enrollment** | [**BirdwatchPublicDataFile**](BirdwatchPublicDataFile.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_public_data_file_bundle import BirdwatchPublicDataFileBundle

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPublicDataFileBundle from a JSON string
birdwatch_public_data_file_bundle_instance = BirdwatchPublicDataFileBundle.from_json(json)
# print the JSON string representation of the object
print(BirdwatchPublicDataFileBundle.to_json())

# convert the object into a dict
birdwatch_public_data_file_bundle_dict = birdwatch_public_data_file_bundle_instance.to_dict()
# create an instance of BirdwatchPublicDataFileBundle from a dict
birdwatch_public_data_file_bundle_from_dict = BirdwatchPublicDataFileBundle.from_dict(birdwatch_public_data_file_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



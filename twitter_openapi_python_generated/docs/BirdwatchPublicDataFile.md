# BirdwatchPublicDataFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**urls** | **List[str]** |  | 

## Example

```python
from twitter_openapi_python_generated.models.birdwatch_public_data_file import BirdwatchPublicDataFile

# TODO update the JSON string below
json = "{}"
# create an instance of BirdwatchPublicDataFile from a JSON string
birdwatch_public_data_file_instance = BirdwatchPublicDataFile.from_json(json)
# print the JSON string representation of the object
print(BirdwatchPublicDataFile.to_json())

# convert the object into a dict
birdwatch_public_data_file_dict = birdwatch_public_data_file_instance.to_dict()
# create an instance of BirdwatchPublicDataFile from a dict
birdwatch_public_data_file_from_dict = BirdwatchPublicDataFile.from_dict(birdwatch_public_data_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



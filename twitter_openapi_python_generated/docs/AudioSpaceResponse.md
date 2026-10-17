# AudioSpaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AudioSpaceData**](AudioSpaceData.md) |  | 
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_response import AudioSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceResponse from a JSON string
audio_space_response_instance = AudioSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceResponse.to_json())

# convert the object into a dict
audio_space_response_dict = audio_space_response_instance.to_dict()
# create an instance of AudioSpaceResponse from a dict
audio_space_response_from_dict = AudioSpaceResponse.from_dict(audio_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



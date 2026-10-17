# AudioSpace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_subscribed** | **bool** |  | 
**metadata** | [**AudioSpaceMetadata**](AudioSpaceMetadata.md) |  | 
**participants** | [**AudioSpaceParticipants**](AudioSpaceParticipants.md) |  | 
**sharings** | [**AudioSpaceSharings**](AudioSpaceSharings.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.audio_space import AudioSpace

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpace from a JSON string
audio_space_instance = AudioSpace.from_json(json)
# print the JSON string representation of the object
print(AudioSpace.to_json())

# convert the object into a dict
audio_space_dict = audio_space_instance.to_dict()
# create an instance of AudioSpace from a dict
audio_space_from_dict = AudioSpace.from_dict(audio_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



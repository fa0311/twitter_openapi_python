# AudioSpaceParticipants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admins** | [**List[AudioSpaceParticipant]**](AudioSpaceParticipant.md) |  | 
**listeners** | [**List[AudioSpaceParticipant]**](AudioSpaceParticipant.md) |  | 
**speakers** | [**List[AudioSpaceParticipant]**](AudioSpaceParticipant.md) |  | 
**total** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_participants import AudioSpaceParticipants

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceParticipants from a JSON string
audio_space_participants_instance = AudioSpaceParticipants.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceParticipants.to_json())

# convert the object into a dict
audio_space_participants_dict = audio_space_participants_instance.to_dict()
# create an instance of AudioSpaceParticipants from a dict
audio_space_participants_from_dict = AudioSpaceParticipants.from_dict(audio_space_participants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



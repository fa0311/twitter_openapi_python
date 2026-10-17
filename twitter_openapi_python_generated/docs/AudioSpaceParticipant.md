# AudioSpaceParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**is_muted_by_admin** | **bool** |  | 
**is_muted_by_guest** | **bool** |  | 
**is_verified** | **bool** |  | 
**periscope_user_id** | **str** |  | 
**start** | **int** |  | [optional] 
**twitter_screen_name** | **str** |  | 
**user_results** | [**AudioSpaceParticipantUserResults**](AudioSpaceParticipantUserResults.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_participant import AudioSpaceParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceParticipant from a JSON string
audio_space_participant_instance = AudioSpaceParticipant.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceParticipant.to_json())

# convert the object into a dict
audio_space_participant_dict = audio_space_participant_instance.to_dict()
# create an instance of AudioSpaceParticipant from a dict
audio_space_participant_from_dict = AudioSpaceParticipant.from_dict(audio_space_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



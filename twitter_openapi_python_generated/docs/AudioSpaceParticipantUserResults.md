# AudioSpaceParticipantUserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_id** | **str** |  | 
**result** | [**AudioSpaceParticipantUser**](AudioSpaceParticipantUser.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_participant_user_results import AudioSpaceParticipantUserResults

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceParticipantUserResults from a JSON string
audio_space_participant_user_results_instance = AudioSpaceParticipantUserResults.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceParticipantUserResults.to_json())

# convert the object into a dict
audio_space_participant_user_results_dict = audio_space_participant_user_results_instance.to_dict()
# create an instance of AudioSpaceParticipantUserResults from a dict
audio_space_participant_user_results_from_dict = AudioSpaceParticipantUserResults.from_dict(audio_space_participant_user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



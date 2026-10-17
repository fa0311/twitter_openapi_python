# AudioSpaceParticipantUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**identity_profile_labels_highlighted_label** | [**IdentityProfileLabelsHighlightedLabel**](IdentityProfileLabelsHighlightedLabel.md) |  | 
**is_blue_verified** | **bool** |  | 
**verification** | [**AudioSpaceParticipantVerification**](AudioSpaceParticipantVerification.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_participant_user import AudioSpaceParticipantUser

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceParticipantUser from a JSON string
audio_space_participant_user_instance = AudioSpaceParticipantUser.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceParticipantUser.to_json())

# convert the object into a dict
audio_space_participant_user_dict = audio_space_participant_user_instance.to_dict()
# create an instance of AudioSpaceParticipantUser from a dict
audio_space_participant_user_from_dict = AudioSpaceParticipantUser.from_dict(audio_space_participant_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



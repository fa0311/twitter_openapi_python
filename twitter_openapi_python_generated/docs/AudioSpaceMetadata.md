# AudioSpaceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**conversation_controls** | **int** |  | 
**created_at** | **int** |  | 
**creator_results** | [**UserResults**](UserResults.md) |  | 
**disallow_join** | **bool** |  | 
**ended_at** | **str** |  | [optional] 
**is_employee_only** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_muted** | **bool** |  | 
**is_space_available_for_clipping** | **bool** |  | 
**is_space_available_for_replay** | **bool** |  | 
**max_admin_capacity** | **int** |  | 
**max_guest_sessions** | **int** |  | 
**media_key** | **str** |  | 
**mentioned_users** | [**List[AudioSpaceMentionedUser]**](AudioSpaceMentionedUser.md) |  | [optional] 
**narrow_cast_space_type** | **int** |  | 
**no_incognito** | **bool** |  | 
**rest_id** | **str** |  | 
**scheduled_start** | **int** |  | [optional] 
**started_at** | **int** |  | 
**state** | **str** |  | 
**title** | **str** |  | 
**total_live_listeners** | **int** |  | 
**total_replay_watched** | **int** |  | 
**tweet_results** | [**ItemResult**](ItemResult.md) |  | 
**updated_at** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.audio_space_metadata import AudioSpaceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AudioSpaceMetadata from a JSON string
audio_space_metadata_instance = AudioSpaceMetadata.from_json(json)
# print the JSON string representation of the object
print(AudioSpaceMetadata.to_json())

# convert the object into a dict
audio_space_metadata_dict = audio_space_metadata_instance.to_dict()
# create an instance of AudioSpaceMetadata from a dict
audio_space_metadata_from_dict = AudioSpaceMetadata.from_dict(audio_space_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



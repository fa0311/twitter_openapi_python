# Broadcast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_for_replay** | **bool** |  | 
**broadcast_id** | **str** |  | 
**camera_rotation** | **int** |  | 
**chat_option** | **int** |  | 
**edited_replay** | [**BroadcastEditedReplay**](BroadcastEditedReplay.md) |  | [optional] 
**end_time** | **int** |  | 
**height** | **int** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**image_url_medium** | **str** |  | 
**image_url_small** | **str** |  | 
**is_high_latency** | **bool** |  | 
**media_key** | **str** |  | 
**periscope_user** | [**BroadcastPeriscopeUser**](BroadcastPeriscopeUser.md) |  | 
**ping_time** | **int** |  | 
**pre_live_slate_url** | **str** |  | [optional] 
**private_chat** | **bool** |  | 
**scheduled_start_time** | **int** |  | [optional] 
**source** | **str** |  | 
**start_time** | **int** |  | 
**state** | **str** |  | 
**status** | **str** |  | 
**total_watched** | **int** |  | 
**total_watching** | **int** |  | 
**tweet_results** | [**ItemResult**](ItemResult.md) |  | 
**user_results** | [**UserResults**](UserResults.md) |  | 
**version** | **int** |  | 
**width** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.broadcast import Broadcast

# TODO update the JSON string below
json = "{}"
# create an instance of Broadcast from a JSON string
broadcast_instance = Broadcast.from_json(json)
# print the JSON string representation of the object
print(Broadcast.to_json())

# convert the object into a dict
broadcast_dict = broadcast_instance.to_dict()
# create an instance of Broadcast from a dict
broadcast_from_dict = Broadcast.from_dict(broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



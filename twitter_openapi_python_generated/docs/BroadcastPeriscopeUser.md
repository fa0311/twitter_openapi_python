# BroadcastPeriscopeUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**profile_image_url** | **str** |  | 
**rest_id** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.broadcast_periscope_user import BroadcastPeriscopeUser

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastPeriscopeUser from a JSON string
broadcast_periscope_user_instance = BroadcastPeriscopeUser.from_json(json)
# print the JSON string representation of the object
print(BroadcastPeriscopeUser.to_json())

# convert the object into a dict
broadcast_periscope_user_dict = broadcast_periscope_user_instance.to_dict()
# create an instance of BroadcastPeriscopeUser from a dict
broadcast_periscope_user_from_dict = BroadcastPeriscopeUser.from_dict(broadcast_periscope_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



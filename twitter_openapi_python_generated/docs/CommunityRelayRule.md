# CommunityRelayRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_relay_rule import CommunityRelayRule

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityRelayRule from a JSON string
community_relay_rule_instance = CommunityRelayRule.from_json(json)
# print the JSON string representation of the object
print(CommunityRelayRule.to_json())

# convert the object into a dict
community_relay_rule_dict = community_relay_rule_instance.to_dict()
# create an instance of CommunityRelayRule from a dict
community_relay_rule_from_dict = CommunityRelayRule.from_dict(community_relay_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



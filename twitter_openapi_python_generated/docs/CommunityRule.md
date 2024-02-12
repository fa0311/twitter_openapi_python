# CommunityRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.community_rule import CommunityRule

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityRule from a JSON string
community_rule_instance = CommunityRule.from_json(json)
# print the JSON string representation of the object
print CommunityRule.to_json()

# convert the object into a dict
community_rule_dict = community_rule_instance.to_dict()
# create an instance of CommunityRule from a dict
community_rule_form_dict = community_rule.from_dict(community_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserResultRelationshipPerspectives


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_by** | **bool** |  | [optional] 
**blocking** | **bool** |  | [optional] 
**followed_by** | **bool** |  | [optional] 
**following** | **bool** |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.user_result_relationship_perspectives import UserResultRelationshipPerspectives

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultRelationshipPerspectives from a JSON string
user_result_relationship_perspectives_instance = UserResultRelationshipPerspectives.from_json(json)
# print the JSON string representation of the object
print(UserResultRelationshipPerspectives.to_json())

# convert the object into a dict
user_result_relationship_perspectives_dict = user_result_relationship_perspectives_instance.to_dict()
# create an instance of UserResultRelationshipPerspectives from a dict
user_result_relationship_perspectives_from_dict = UserResultRelationshipPerspectives.from_dict(user_result_relationship_perspectives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



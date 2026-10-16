# UserRelationshipCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**followers** | **int** |  | 
**following** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_relationship_counts import UserRelationshipCounts

# TODO update the JSON string below
json = "{}"
# create an instance of UserRelationshipCounts from a JSON string
user_relationship_counts_instance = UserRelationshipCounts.from_json(json)
# print the JSON string representation of the object
print(UserRelationshipCounts.to_json())

# convert the object into a dict
user_relationship_counts_dict = user_relationship_counts_instance.to_dict()
# create an instance of UserRelationshipCounts from a dict
user_relationship_counts_from_dict = UserRelationshipCounts.from_dict(user_relationship_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



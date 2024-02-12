# AuthorCommunityRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_results** | [**Community**](Community.md) |  | 
**role** | **str** |  | [optional] 
**user_results** | [**UserResults**](UserResults.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.author_community_relationship import AuthorCommunityRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorCommunityRelationship from a JSON string
author_community_relationship_instance = AuthorCommunityRelationship.from_json(json)
# print the JSON string representation of the object
print AuthorCommunityRelationship.to_json()

# convert the object into a dict
author_community_relationship_dict = author_community_relationship_instance.to_dict()
# create an instance of AuthorCommunityRelationship from a dict
author_community_relationship_form_dict = author_community_relationship.from_dict(author_community_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ListMembersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_timeline** | [**TimelineResult**](TimelineResult.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_members_list import ListMembersList

# TODO update the JSON string below
json = "{}"
# create an instance of ListMembersList from a JSON string
list_members_list_instance = ListMembersList.from_json(json)
# print the JSON string representation of the object
print(ListMembersList.to_json())

# convert the object into a dict
list_members_list_dict = list_members_list_instance.to_dict()
# create an instance of ListMembersList from a dict
list_members_list_from_dict = ListMembersList.from_dict(list_members_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



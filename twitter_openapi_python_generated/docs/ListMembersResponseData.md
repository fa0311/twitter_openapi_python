# ListMembersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ListMembersList**](ListMembersList.md) |  | 

## Example

```python
from twitter_openapi_python_generated.models.list_members_response_data import ListMembersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListMembersResponseData from a JSON string
list_members_response_data_instance = ListMembersResponseData.from_json(json)
# print the JSON string representation of the object
print(ListMembersResponseData.to_json())

# convert the object into a dict
list_members_response_data_dict = list_members_response_data_instance.to_dict()
# create an instance of ListMembersResponseData from a dict
list_members_response_data_from_dict = ListMembersResponseData.from_dict(list_members_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



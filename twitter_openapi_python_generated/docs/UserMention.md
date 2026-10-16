# UserMention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**id_str** | **str** |  | 
**indices** | **List[int]** |  | 
**name** | **str** |  | 
**screen_name** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_mention import UserMention

# TODO update the JSON string below
json = "{}"
# create an instance of UserMention from a JSON string
user_mention_instance = UserMention.from_json(json)
# print the JSON string representation of the object
print(UserMention.to_json())

# convert the object into a dict
user_mention_dict = user_mention_instance.to_dict()
# create an instance of UserMention from a dict
user_mention_from_dict = UserMention.from_dict(user_mention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



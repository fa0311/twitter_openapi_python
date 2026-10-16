# UserLabelMentionUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typename** | [**TypeName**](TypeName.md) |  | 
**core** | [**UserLabelMentionUserCore**](UserLabelMentionUserCore.md) |  | 
**rest_id** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label_mention_user import UserLabelMentionUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabelMentionUser from a JSON string
user_label_mention_user_instance = UserLabelMentionUser.from_json(json)
# print the JSON string representation of the object
print(UserLabelMentionUser.to_json())

# convert the object into a dict
user_label_mention_user_dict = user_label_mention_user_instance.to_dict()
# create an instance of UserLabelMentionUser from a dict
user_label_mention_user_from_dict = UserLabelMentionUser.from_dict(user_label_mention_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



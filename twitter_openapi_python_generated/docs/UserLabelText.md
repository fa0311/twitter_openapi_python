# UserLabelText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[UserLabelTextEntity]**](UserLabelTextEntity.md) |  | 
**text** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label_text import UserLabelText

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabelText from a JSON string
user_label_text_instance = UserLabelText.from_json(json)
# print the JSON string representation of the object
print(UserLabelText.to_json())

# convert the object into a dict
user_label_text_dict = user_label_text_instance.to_dict()
# create an instance of UserLabelText from a dict
user_label_text_from_dict = UserLabelText.from_dict(user_label_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



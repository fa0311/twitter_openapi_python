# UserLabelTextEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_index** | **int** |  | 
**ref** | [**UserLabelTextEntityRef**](UserLabelTextEntityRef.md) |  | 
**to_index** | **int** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label_text_entity import UserLabelTextEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabelTextEntity from a JSON string
user_label_text_entity_instance = UserLabelTextEntity.from_json(json)
# print the JSON string representation of the object
print(UserLabelTextEntity.to_json())

# convert the object into a dict
user_label_text_entity_dict = user_label_text_entity_instance.to_dict()
# create an instance of UserLabelTextEntity from a dict
user_label_text_entity_from_dict = UserLabelTextEntity.from_dict(user_label_text_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



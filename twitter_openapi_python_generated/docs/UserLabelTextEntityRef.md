# UserLabelTextEntityRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mention_results** | [**UserLabelMentionResults**](UserLabelMentionResults.md) |  | 
**screen_name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from twitter_openapi_python_generated.models.user_label_text_entity_ref import UserLabelTextEntityRef

# TODO update the JSON string below
json = "{}"
# create an instance of UserLabelTextEntityRef from a JSON string
user_label_text_entity_ref_instance = UserLabelTextEntityRef.from_json(json)
# print the JSON string representation of the object
print(UserLabelTextEntityRef.to_json())

# convert the object into a dict
user_label_text_entity_ref_dict = user_label_text_entity_ref_instance.to_dict()
# create an instance of UserLabelTextEntityRef from a dict
user_label_text_entity_ref_from_dict = UserLabelTextEntityRef.from_dict(user_label_text_entity_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


